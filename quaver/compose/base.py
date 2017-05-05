import abc

from typing import List, TypeVar

from quaver.play.block import Block
from quaver.compose.constants import FRAME_RATE


class _Playable(object):
    __metaclass__ = abc.ABCMeta

    duration: int = 0
    volume: float = 0.25

    @abc.abstractmethod
    def to_sound(self, tempo=60, volume=1) -> Block:
        pass

    @property
    @abc.abstractmethod
    def len(self):
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

    def __gt__(self, other):
        if isinstance(other, (tuple, list)) and len(other) == 2:
            tempo, volume = other
        elif isinstance(other, dict):
            tempo = other.get('tempo', 60)
            volume = other.get('volume', 1)
        elif isinstance(other, (int, float)):
            tempo = other
            volume = 1
        else:
            tempo = 60
            volume = 1
        self.play(tempo=tempo, volume=volume)


T = TypeVar('T', covariant=_Playable)


def _duration_suffix(duration):
    if duration == FRAME_RATE:
        suffix = ''
    else:
        if duration > FRAME_RATE:
            op = ' * '
            num = duration / FRAME_RATE
        else:
            op = ' / '
            num = FRAME_RATE / duration
        if round(num, 1) == num:
            suffix = op + str(int(num))
        else:
            suffix = op + str(num)
    return suffix
