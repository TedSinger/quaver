import os
import abc
import math
import wave
import numpy
import tempfile
import subprocess
from quaver.compose.constants import FRAME_RATE

CLIP_FRAMES = 256


class Block(object):
    @property
    @abc.abstractmethod
    def array(self) -> numpy.array:
        return numpy.zeros(1)

    def to_bytes(self):
        arr = self.array
        m = max(abs(arr))
        if m > 1:
            print('Warning: too loud. The waveform will be scaled down by a factor of {m:.2}'.format(m=m))
            arr /= m
        return (arr * (2 ** 15 - 1)).astype('int16').tobytes()

    @classmethod
    def beep(cls, frames: int, frequency, start_amplitude, stop_amplitude):
        return LazyBlock(lambda: beep_array(frames, frequency, start_amplitude, stop_amplitude), 0)

    @classmethod
    def silence(cls, frames: int):
        return LazyBlock(lambda: numpy.zeros(frames), 0)

    def to_wav(self, filename, nchannels=1, sample_width=2, compression_type='NONE', compression_name='no compression'):
        with open(filename, 'wb') as f:
            with wave.open(f) as w:
                w.setparams((
                    nchannels,
                    sample_width,
                    FRAME_RATE,
                    0,
                    compression_type,
                    compression_name
                ))
                w.setnframes((0xFFFFFFFF - 36) // w.getnchannels() // w.getsampwidth())
                w.writeframesraw(self.to_bytes())

    def play(self):
        # *nix (and possibly Ubuntu) specific
        f = tempfile.NamedTemporaryFile('wb', delete=False)
        f.close()
        self.to_wav(f.name)
        try:
            subprocess.call(['play', '-t', 'wav', f.name])
        finally:
            os.unlink(f.name)


class NumpyBlock(Block):
    def __init__(self, arr, start_frame):
        self._arr = arr
        self.start_frame = start_frame
        self.end_frame = start_frame + len(arr)

    @property
    def array(self):
        return self._arr


class LazyBlock(Block):
    def __init__(self, fn, start_frame):
        self._fn = fn
        self._arr = None
        self.start_frame = start_frame

    @property
    def array(self):
        if self._arr is None:
            self._arr = self._fn()
            assert isinstance(self._arr, numpy.ndarray)
        return self._arr

    @property
    def end_frame(self):
        return self.start_frame + len(self.array)


class CollectionBlock(Block):
    def __init__(self, blocks, start_frame):
        self.blocks = blocks
        self.start_frame = start_frame

    @property
    def array(self):
        length = max([b.end_frame for b in self.blocks])
        ret = numpy.zeros(length)
        for b in self.blocks:
            ret[b.start_frame:b.end_frame] += b.array
        return ret

    @property
    def end_frame(self):
        return self.start_frame + len(self.array)


def memoize(fn):
    cache = {}

    def new_fn(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return new_fn


@memoize
def distortion(frames: int):
    """
    Something like vibrato 
    """
    pivot = math.pi * 7 / 4
    part_one = numpy.linspace(start=0, stop=pivot, num=FRAME_RATE // 4)
    if frames > FRAME_RATE // 4:
        part_two = numpy.linspace(start=pivot, stop=pivot + math.pi * 17 * (frames / FRAME_RATE - 1 / 4.),
                                  num=frames - FRAME_RATE // 4)
        total = numpy.zeros(frames)
        total[:FRAME_RATE // 4] = part_one
        total[FRAME_RATE // 4:] = part_two
    else:
        total = part_one[:frames]
    numpy.sin(total, out=total)
    total *= .005
    total += 1
    return total


@memoize
def beep_array(frames: int, frequency, start_amplitude, stop_amplitude):
    arr = numpy.zeros(frames)
    arr += frequency * 2 * math.pi / FRAME_RATE
    arr *= distortion(frames)
    arr.cumsum(out=arr)
    numpy.sin(arr, out=arr)
    arr[-CLIP_FRAMES:] *= numpy.linspace(start=1, stop=0, num=CLIP_FRAMES)
    arr[:CLIP_FRAMES] *= numpy.linspace(start=0, stop=1, num=CLIP_FRAMES)
    arr *= numpy.linspace(start=start_amplitude, stop=stop_amplitude, num=frames)
    return arr
