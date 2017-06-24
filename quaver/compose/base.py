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
            return self.fn(playable, *self.args, **self.kwargs)
        elif isinstance(playable, tuple):
            return tuple(self(entry) for entry in playable)
        elif isinstance(playable, set):
            return set(self(entry) for entry in playable)
        elif isinstance(playable, dict):
            return dict((key, self(value)) for key, value in playable.items())
        else:
            raise TypeError(playable)


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

class Rational(PartialRecursive):
    def __init__(self, num, den):
        super(Rational, self).__init__(lambda p: p._with('len', self))
        g = _gcf(num, den)
        self.num = num // g
        self.den = den // g

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
    volume: float = 0.25

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
