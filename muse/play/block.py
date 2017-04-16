import abc
import math
import numpy
from muse.play.output import play
from muse.compose.constants import FRAME_RATE


class Block(object):
    @property
    @abc.abstractmethod
    def array(self) -> numpy.array:
        return numpy.zeros(1)

    def to_bytes(self):
        return (self.array * (2 ** 15 - 1)).astype('int16').tobytes()

    @classmethod
    def beep(cls, frames, frequency, amplitude):
        return LazyBlock(lambda: beep_array(frames, frequency, amplitude), 0)

    @classmethod
    def silence(cls, frames: int):
        return LazyBlock(lambda: numpy.zeros(frames), 0)

    def play(self):
        play(self.to_bytes())


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


_BEEPS = {}


def beep_array(frames, frequency, amplitude):
    if (frames, frequency, amplitude) not in _BEEPS:
        _BEEPS[(frames, frequency, amplitude)] = _beep_array(frames, frequency, amplitude)
    return _BEEPS[(frames, frequency, amplitude)]


def _beep_array(frames, frequency, amplitude):
    stop = 2 * math.pi * frequency * (frames - 1) / FRAME_RATE
    arr = numpy.linspace(start=0, stop=stop, num=frames)
    numpy.sin(arr, out=arr)
    arr[-256:] *= numpy.linspace(start=1, stop=0, num=256)
    arr[:256] *= numpy.linspace(start=0, stop=1, num=256)
    arr *= amplitude
    return arr
