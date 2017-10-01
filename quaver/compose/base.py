import abc

from typing import TypeVar
from quaver.play.block import Block


def _gcf(a, b):
    if b > a:
        return _gcf(b, a)
    elif b == 0:
        return a
    else:
        return _gcf(b, a % b)


class PartialRecursive(object):
    def __init__(self, fn, *args, **kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def __call__(self, playable):
        if isinstance(playable, _Playable):
            return self._on_playable(playable)
        elif isinstance(playable, tuple):
            return self._on_tuple(playable)
        elif isinstance(playable, set):
            return self._on_set(playable)
        elif isinstance(playable, dict):
            return self._on_dict(playable)
        else:
            raise TypeError(playable)

    def _on_playable(self, p):
        return self.fn(p, *self.args, **self.kwargs)

    def _on_tuple(self, tup):
        return tuple(self(entry) for entry in tup)

    def _on_set(self, st):
        return set(self(entry) for entry in st)

    def _on_dict(self, dt):
        return dict((key, self(value)) for key, value in dt.items())

    def __pow__(self, other):
        if isinstance(other, PartialRecursive):
            return PartialRecursive(lambda p: self(other(p)))
        else:
            return self(other)


class Longer(PartialRecursive):
    def __init__(self, by):
        super(Longer, self).__init__(lambda p, by: p.longer(by), by)


class Shorter(PartialRecursive):
    def __init__(self, by):
        super(Shorter, self).__init__(lambda p, by: p.shorter(by), by)


class Louder(PartialRecursive):
    def __init__(self, by):
        super(Louder, self).__init__(lambda p, by: p.louder(by), by)


class Softer(PartialRecursive):
    def __init__(self, by):
        super(Softer, self).__init__(lambda p, by: p.softer(by), by)


class T(PartialRecursive):
    def __init__(self, by):
        super(T, self).__init__(lambda p, by: p.T(by), by)


class _Staccato(PartialRecursive):
    def __init__(self):
        super(_Staccato, self).__init__(lambda p: p.staccato)
Staccato = _Staccato()


def get_len(playable):
    if isinstance(playable, _Playable):
        return playable.len
    elif isinstance(playable, tuple):
        return sum(map(get_len, playable), Rational(0, 1))
    elif isinstance(playable, set):
        return max(map(get_len, playable))
    elif isinstance(playable, dict):
        return max(map(get_len, playable.values()))
    else:
        raise TypeError(playable)


class Crescendo(PartialRecursive):
    def __init__(self, by):
        super(Crescendo, self).__init__(lambda p, by: p.cresc(by), by)
        self.by = by

    def _on_tuple(self, tup):
        lens = [get_len(p).to_float() for p in tup]
        total = sum(lens)
        vols = []
        cursor = 1.
        for l in lens:
            vols.append(cursor)
            cursor += (l * (self.by - 1) / total)
        vols.append(self.by)
        parts = []
        for i, p in enumerate(tup):
            parts.append(Crescendo(vols[i + 1] / vols[i])(Louder(vols[i])(p)))
        return tuple(parts)


def Decrescendo(by):
    return Crescendo(1. / by)


class Rational(PartialRecursive):
    def __init__(self, num, den):
        super(Rational, self).__init__(lambda p: p._with('len', self))
        g = _gcf(num, den)
        self.num = num // g
        self.den = den // g

    def to_float(self):
        return float(self.num) / self.den

    def __gt__(self, other):
        return self.num * other.den > other.num * self.den

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.num + other * self.den, self.den)
        elif isinstance(other, Rational):
            return Rational(self.num * other.den + self.den * other.num, self.den * other.den)
        elif isinstance(other, float):
            return other * self.num / self.den
        else:
            raise

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.num * other, self.den)
        elif isinstance(other, Rational):
            return Rational(self.num * other.num, self.den * other.den)
        elif isinstance(other, float):
            return other * self.num / self.den
        else:
            raise

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self.num, self.den * other)
        elif isinstance(other, Rational):
            return Rational(self.num * other.den, self.den * other.num)
        elif isinstance(other, float):
            return self.num / (self.den * other)
        else:
            raise

    def __hash__(self):
        return hash(self.num) * hash(self.den)

    def __repr__(self):
        if self == QUARTER:
            return ''
        elif self.num == 1:
            return '._' + str(self.den)
        else:
            return '._%s_%s' % (self.num, self.den)


WHOLE = Rational(1, 1)
HALF = Rational(1, 2)
QUARTER = Rational(1, 4)
EIGHTH = Rational(1, 8)
SIXTEENTH = Rational(1, 16)


class _Playable(object):
    __metaclass__ = abc.ABCMeta

    len: Rational = Rational(0, 1)
    start_volume: float = 0.25
    stop_volume: float = 0.25

    @abc.abstractmethod
    def to_sound(self, tempo=60, volume=1) -> Block:
        pass

    @abc.abstractmethod
    def T(self, half_steps: int) -> '_Playable':
        return self

    def __neg__(self) -> '_Playable':
        return self.T(-1)

    def __pos__(self) -> '_Playable':
        return self.T(1)

    def play(self, tempo=60, volume=1):
        self.to_sound(tempo=tempo, volume=volume).play()


_SubPlayable = TypeVar('T', covariant=_Playable)
