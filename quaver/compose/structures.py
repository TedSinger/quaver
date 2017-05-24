import abc
from functools import reduce

from quaver.compose.base import _Playable, _duration_suffix
from quaver.compose.constants import FRAME_RATE
from quaver.play.block import CollectionBlock, Block


class _Collection(_Playable):
    __metaclass__ = abc.ABCMeta

    def __init__(self, *notes: _Playable):
        self.notes = ()
        for n in notes:
            # this merging simplifies the structure, but is that really a good thing?
            # PRO: flat is better than nested
            # CON: the composer *wrote* the music with that structure and probably wants to *see* that structure
            if isinstance(n, self.__class__):
                self.notes += n.notes
            else:
                self.notes += (n,)

    def __iter__(self):
        return iter(self.notes)

    def T(self, half_steps: int) -> '_Collection':
        return self.__class__(*[n.T(half_steps) for n in self])

    def __truediv__(self, other: float) -> '_Collection':
        return self.__class__(*[n / other for n in self])

    def __mul__(self, other: float) -> '_Collection':
        return self.__class__(*[n * other for n in self])

    def __mod__(self, other: float) -> '_Collection':
        return self.__class__(*[n % other for n in self])

    def __xor__(self, other: float) -> '_Collection':
        return self.__class__(*[n ^ other for n in self])

    @property
    def staccato(self) -> '_Collection':
        return self.__class__(*[n.staccato for n in self])

    def _gcf(self):
        if len(self.notes) == 1:
            return self.notes[0].len
        else:
            return reduce(_gcf, [n.len for n in self])

    def __repr__(self):
        note_str = ', '.join(map(str, (self / self._gcf()).notes))
        duration_str = _duration_suffix(FRAME_RATE * self._gcf())
        # need a suffix for volume!
        return self.__class__.__name__ + '(' + note_str + ')' + duration_str

    def _combine(self, other, cls):
        notes = []
        for obj in [self, other]:
            if isinstance(obj, cls):
                notes.extend(obj.notes)
            else:
                notes.append(obj)
        return cls(*notes)

    def _rcombine(self, other, cls):
        notes = []
        for obj in [other, self]:
            if isinstance(obj, cls):
                notes.extend(obj.notes)
            else:
                notes.append(obj)
        return cls(*notes)

    def __and__(self, other: _Playable) -> 'Chord':
        return self._combine(other, Chord)

    def __rand__(self, other: _Playable) -> 'Chord':
        return self._rcombine(other, Chord)

    def __or__(self, other: _Playable) -> 'Stanza':
        return self._combine(other, Stanza)

    def __ror__(self, other: _Playable) -> 'Stanza':
        return self._rcombine(other, Stanza)

    def __neg__(self):
        return self.T(-1)

    def __pos__(self):
        return self.T(1)

    def x(self, other: int):
        assert isinstance(other, int)
        return Stanza(*[self for i in range(other)])

    def __eq__(self, other):
        # FIXME: _Collections of 1, and Chords are commutative
        return isinstance(other, self.__class__) and self.notes == other.notes


class Chord(_Collection):
    def to_sound(self, tempo=60, volume=1) -> Block:
        return CollectionBlock([n.to_sound(tempo=tempo, volume=volume) for n in self], 0)

    @property
    def len(self):
        return max([n.len for n in self])

    @property
    def splayed(self):
        return Stanza(*self.notes) / len(self.notes)


class Stanza(_Collection):
    def to_sound(self, tempo=60, volume=1) -> Block:
        blocks = []
        start_frame = 0
        for n in self:
            s = n.to_sound(tempo=tempo, volume=volume)
            s.start_frame = start_frame
            blocks.append(s)
            start_frame += len(s.array)
        return CollectionBlock(blocks, 0)

    @property
    def len(self):
        return sum([n.len for n in self] + [0])

    @property
    def stacked(self):
        return Chord(*self.notes) * len(self.notes)


def _gcf(a, b):
    if b > a:
        return _gcf(b, a)
    elif b == 0:
        return a
    else:
        return _gcf(b, a % b)
