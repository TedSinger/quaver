from quaver.compose import D4
from quaver.compose.structures import Stanza


class Key(object):
    def __init__(self, root):
        self.root = root

    def __contains__(self, note):
        return ((note.halves_above_C4 - self.root.halves_above_C4) % 12) in self.ALLOWED_DIFFS

    def __getitem__(self, slc: slice):
        total_halves = slc.stop.halves_above_C4 - slc.start.halves_above_C4
        if total_halves > 0:
            candidates = [slc.start.T(i) for i in range(0, total_halves + 1)]
        else:
            candidates = [slc.start.T(-i) for i in range(0, - total_halves + 1)]
        return Stanza(*[c for c in candidates if c in self])


class MajorKey(Key):
    ALLOWED_DIFFS = [0, 2, 4, 5, 7, 9, 11]


class MinorKey(Key):
    ALLOWED_DIFFS = [0, 2, 3, 5, 7, 8, 10]


DMaj = MajorKey(D4)