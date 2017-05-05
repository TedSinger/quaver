from math import log
import abc
from typing import List, TypeVar
from quaver.compose.base import _Playable, _duration_suffix, T
from quaver.compose.constants import _C4_FREQ, OCTAVE, _HALF_STEP_INTERVAL, MAJ_6, MIN_7, MAJ_3, MAJ_7, PFT_5, MIN_3, \
    MIN_6, FRAME_RATE
from quaver.compose.structure import Stanza, Chord
from quaver.play.block import Block


class _Constant(_Playable):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def _copy(self: T) -> T:
        pass

    def _with(self: T, attr: str, value) -> T:
        a = self._copy()
        setattr(a, attr, value)
        return a

    def split(self, t) -> List[_Playable]:
        assert t < self.len
        a = round(t * FRAME_RATE)
        b = self.duration - a
        return [self._with('duration', a), self._with('duration', b)]

    @property
    def len(self):
        return float(self.duration) / FRAME_RATE

    def x(self, n: int) -> Stanza:
        return Stanza(*[self for i in range(n)])

    def __mul__(self: T, other: float) -> T:
        return self._with('duration', self.duration * other)

    def __truediv__(self: T, other: float) -> T:
        return self * (1. / other)

    def __xor__(self: T, other: float) -> T:
        return self._with('volume', self.volume * other)

    def __mod__(self: T, other: float) -> T:
        return self ^ (1. / other)

    def __or__(self, other) -> Stanza:
        if isinstance(other, Stanza):
            return Stanza(self, *other.notes)
        else:
            return Stanza(self, other)

    def __and__(self, other) -> Chord:
        if isinstance(other, Chord):
            return Chord(self, *other.notes)
        else:
            return Chord(self, other)


class Silence(_Constant):
    def __init__(self, duration=FRAME_RATE):
        self.duration = duration

    def _copy(self) -> 'Silence':
        return Silence(self.duration)

    def to_sound(self, tempo=60, volume=1) -> Block:
        return Block.silence(int(self.len * 60. * FRAME_RATE / tempo))

    def T(self, half_steps) -> 'Silence':
        return self

    @property
    def staccato(self):
        return self

    def __repr__(self):
        return 'Z' + _duration_suffix(self.duration)


class Note(_Constant):
    def __init__(self, freq, duration=FRAME_RATE, volume=.25):
        self._freq = freq
        self.duration = duration
        self.volume = volume

    def _copy(self) -> 'Note':
        return Note(self._freq, self.duration, self.volume)

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
        return tone + _duration_suffix(self.duration)

    def to_sound(self, tempo=60, volume=1) -> Block:
        return Block.beep(self.len * 60. * FRAME_RATE / tempo, self._freq,
                          volume * self.volume * (220 / self._freq) ** 1.25)

    @property
    def staccato(self):
        return (self | (Silence() * self.len)) / 2

    def trill(self, n: int):
        atempo = self._with('duration', FRAME_RATE / 16)
        s = Stanza(atempo, atempo.T(n))
        return atempo * 3 | atempo.T(n) * 2 | \
               s.x(round((self.duration - atempo.duration * 6) / (2 * atempo.duration))) | \
               atempo

    @property
    def maj(self) -> Chord:
        return self & self.T(MAJ_3) & self.T(PFT_5)

    @property
    def maj6(self) -> Chord:
        return self.maj & self.T(MAJ_6)

    @property
    def maj7(self) -> Chord:
        return self.maj & self.T(MAJ_7)

    @property
    def dom7(self) -> Chord:
        return self.maj & self.T(MIN_7)

    @property
    def min(self) -> Chord:
        return self & self.T(MIN_3) & self.T(PFT_5)

    @property
    def min6(self) -> Chord:
        return self.min & self.T(MAJ_6)

    @property
    def min7(self) -> Chord:
        return self.min & self.T(MIN_7)

    @property
    def minmaj7(self) -> Chord:
        return self.min & self.T(MAJ_7)

    @property
    def aug(self) -> Chord:
        return self & self.T(MAJ_3) & self.T(MIN_6)

    @property
    def aug7(self) -> Chord:
        return self.aug & self.T(MIN_7)

    @property
    def dim(self) -> Chord:
        return self & self.T(MIN_3) & self.T(PFT_5 - 1)

    @property
    def dim7(self) -> Chord:
        return self.dim & self.T(MAJ_6)
