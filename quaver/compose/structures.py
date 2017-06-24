from quaver.compose.base import _Playable
from quaver.play.block import CollectionBlock


def flatten(playable):
    if isinstance(playable, _Playable):
        return playable
    elif isinstance(playable, tuple):
        ret = ()
        for p in playable:
            part = flatten(p)
            if isinstance(part, tuple):
                ret += part
            else:
                ret += (part,)
        if len(ret) == 1:
            return ret[0]
        else:
            return ret
    elif isinstance(playable, set):
        return set(flatten(p) for p in playable)
    elif isinstance(playable, dict):
        return dict((k, flatten(v)) for k, v in playable.items())
    else:
        raise TypeError(playable)


def _stanza_to_sound(stanza, tempo=60, volume=1):
    blocks = []
    start_frame = 0
    for n in stanza:
        s = to_sound(n, tempo=tempo, volume=volume)
        s.start_frame = start_frame
        blocks.append(s)
        start_frame += len(s.array)
    return CollectionBlock(blocks, 0)


def _chord_to_sound(chord, tempo=60, volume=1):
    return CollectionBlock([to_sound(n, tempo=tempo, volume=volume) for n in chord], 0)


def _score_to_sound(score, tempo=60, volume=1):
    return _chord_to_sound(score.values(), tempo=tempo, volume=volume)


def _note_to_sound(note, tempo=60, volume=1):
    return note.to_sound(tempo=tempo, volume=volume)


def to_sound(playable, tempo=60, volume=1):
    if isinstance(playable, _Playable):
        return _note_to_sound(playable, tempo=tempo, volume=volume)
    elif isinstance(playable, tuple):
        return _stanza_to_sound(playable, tempo=tempo, volume=volume)
    elif isinstance(playable, set):
        return _chord_to_sound(playable, tempo=tempo, volume=volume)
    elif isinstance(playable, dict):
        return _score_to_sound(playable, tempo=tempo, volume=volume)
    else:
        raise TypeError(playable)


def play(playable, tempo=60, volume=1):
    to_sound(flatten(playable), tempo=tempo, volume=volume).play()


def to_wav(playable, filename, tempo=60, volume=1):
    to_sound(flatten(playable), tempo=tempo, volume=volume).to_wav(filename)
