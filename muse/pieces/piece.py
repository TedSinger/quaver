from muse.compose.notes import *

MAJOR_LINE = Stanza(D5, A4, +F4, A4) / 4
MINOR_LINE = Stanza(+C5, A4, G4, A4) / 4
SONG = Chord(MAJOR_LINE.staccato.x(4) | MINOR_LINE.staccato.x(4), Stanza(A3 * 4, E3 * 4))

ARPEGGIO = (A3.maj | A4.maj | A5 * 2).splayed

FOUR_CHORD_SONG = Stanza(C4.maj, G3.maj, A3.min, F3.maj)
