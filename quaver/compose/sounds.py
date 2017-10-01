from math import log
import abc
from typing import List, TypeVar, Tuple, Set, Iterable
from quaver.compose.base import _Playable, _SubPlayable, QUARTER, Rational
from quaver.compose.constants import _C4_FREQ, OCTAVE, FRAME_RATE, _HALF_STEP_INTERVAL, MAJ_6, MIN_7, MAJ_3, MAJ_7, \
    PFT_5, MIN_3, \
    MIN_6
from quaver.play.block import Block
import re

class _Constant(_Playable):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _copy(self: _SubPlayable) -> '_Constant':
        pass

    def _with(self: _SubPlayable, attr: str, value) -> '_Constant':
        a = self._copy()
        setattr(a, attr, value)
        return a

    def split(self, t) -> Tuple['_Constant', '_Constant']:
        assert t < self.len
        return (self._with('duration', t), self._with('duration', self.len - t))

    def __mul__(self, n: int) -> Iterable['_Constant']:
        return tuple(self for i in range(n))

    def __getattr__(self, name):
        t1 = re.match('^_(\d+)$', name)
        if t1:
            den = t1.groups()[0]
            return self._with('len', Rational(1, int(den)))
        else:
            t2 = re.match('^_(\d+)_(\d+)', name)
            if t2:
                num, den = t2.groups()
                return self._with('len', Rational(int(num), int(den)))
            else:
                raise AttributeError('Unknown attribute %s' % name)


    def longer(self: _SubPlayable, other: int) -> _SubPlayable:
        return self._with('len', self.len * other)

    def shorter(self: _SubPlayable, other: int) -> _SubPlayable:
        return self._with('len', self.len / other)

    def louder(self: _SubPlayable, other: float) -> _SubPlayable:
        return self._with('start_volume', self.start_volume * other)._with('stop_volume', self.stop_volume * other)

    def softer(self: _SubPlayable, other: float) -> _SubPlayable:
        return self.louder(1. / other)

    def cresc(self: _SubPlayable, other: float) -> _SubPlayable:
        return self._with('stop_volume', self.stop_volume * other)

    def decresc(self: _SubPlayable, other: float) -> _SubPlayable:
        return self.cresc(1. / other)

    def __eq__(self, other):
        # FIXME: iffy
        return str(self) == str(other)

    def __lt__(self, other):
        if isinstance(other, Silence):
            return False
        elif isinstance(other, Note):
            if isinstance(self, Note):
                return self._freq < other._freq
            else:
                return True
        else:
            raise


class Silence(_Constant):
    def __init__(self, len=QUARTER):
        self.len = len

    def _copy(self) -> 'Silence':
        return Silence(self.len)

    def to_sound(self, tempo=60, volume=1) -> Block:
        return Block.silence(int(self.len * 4 * 60. * FRAME_RATE / tempo))

    def T(self, half_steps) -> 'Silence':
        return self

    @property
    def staccato(self):
        return self

    def __repr__(self):
        return 'Z' + str(self.len)

    def __hash__(self):
        return hash(self.len)


class Note(_Constant):
    def __init__(self, freq, len=QUARTER, start_volume=.25, stop_volume=0.25):
        self._freq = freq
        self.len = len
        self.start_volume = start_volume
        self.stop_volume = stop_volume

    def __hash__(self):
        return int(self._freq) + hash(self.len) + int(self.start_volume * 300) + int(self.stop_volume * 555)

    def _copy(self) -> 'Note':
        return Note(self._freq, self.len, self.start_volume, self.stop_volume)

    def T(self, half_steps):
        return self._with('_freq', self._freq * _HALF_STEP_INTERVAL ** half_steps)

    @property
    def halves_above_C4(self):
        return int(round(log(self._freq / _C4_FREQ) / log(_HALF_STEP_INTERVAL)))

    def __repr__(self):
        half_steps = self.halves_above_C4
        octave = 4 + half_steps // OCTAVE
        note = 'CCDDEFFGGAAB'[half_steps % OCTAVE]
        sharp = '010100101010'[half_steps % OCTAVE]
        tone = ('+' if int(sharp) else '') + note + str(octave)
        # FIXME: need a suffix for volume!
        return tone + str(self.len)


    def to_sound(self, tempo=60, volume=1) -> Block:
        return Block.beep(int(self.len * 4 * 60. * FRAME_RATE / tempo),
                          self._freq,
                          volume * self.start_volume * (220 / self._freq) ** 1.25,
                          volume * self.stop_volume * (220 / self._freq) ** 1.25)

    @property
    def staccato(self):
        return (self._with('len', self.len / 2), Silence(self.len / 2))

    @property
    def maj(self) -> Set['Note']:
        return {self, self.T(MAJ_3), self.T(PFT_5)}

    @property
    def maj6(self) -> Set['Note']:
        return self.maj | {self.T(MAJ_6)}

    @property
    def maj7(self) -> Set['Note']:
        return self.maj | {self.T(MAJ_7)}

    @property
    def dom7(self) -> Set['Note']:
        return self.maj | {self.T(MIN_7)}

    @property
    def min(self) -> Set['Note']:
        return {self, self.T(MIN_3), self.T(PFT_5)}

    @property
    def min6(self) -> Set['Note']:
        return self.min | {self.T(MAJ_6)}

    @property
    def min7(self) -> Set['Note']:
        return self.min | {self.T(MIN_7)}

    @property
    def minmaj7(self) -> Set['Note']:
        return self.min | {self.T(MAJ_7)}

    @property
    def aug(self) -> Set['Note']:
        return {self, self.T(MAJ_3), self.T(MIN_6)}

    @property
    def aug7(self) -> Set['Note']:
        return self.aug | {self.T(MIN_7)}

    @property
    def dim(self) -> Set['Note']:
        return {self, self.T(MIN_3), self.T(PFT_5 - 1)}

    @property
    def dim7(self) -> Set['Note']:
        return self.dim | {self.T(MAJ_6)}
