from muse.compose.notes import *
from muse.compose.keys import MajorKey

KEY = MajorKey(D4)

BASE = Stanza(D3, A2, B2, +F2, G2, D2, G2, A2)

VOICE_1 = Stanza(+F4, E4, D4, +C4, B3, A3, B3, +C4,
                 D4, +C4, B3, A3, G3, +F3, G3, E3).T(12)
VOICE_2 = Stanza(D3, +F3, A3, G3, +F3, D3, +F3, E3,
                 D3, B2, D3, A3, G3, B3, A3, G3,
                 +F3, D3, E3, +C4, D4, +F4, A4, A3,
                 B3, G3, A3, +F3, D3, D4, (D4 * 3 / 2).trill(2), +C4 / 2).T(12) / 2

VOICE_3 = Stanza(D5, +C5, D5, D4, +C4, A4, E4, +F4, D4, D5, +C5, B4, +C5, +F5, A5, B5, G5, +F5, E5, G5, +F5,
                 E5, D5, +C5, B4, A4, G4, +F4, E4, G4, +F4, E4, D4, E4, +F4, G4, A4, E4, A4, G4, +F4, B4, A4,
                 G4, A4, G4, +F4, E4, D4, B3, B4, +C5, D5, +C5, B4, A4, G4, +F4, E4, B4, A4, B4, A4, G4) / 4

VOICE_4 = Stanza(+F4, +F5, E5 * 2, Z, D5, +F5 * 2,
                 B5 * 2, A5 * 2, B5 * 2, +C6 * 2,
                 D6, D5, +C5 * 2, Z, B4, D5 * 2,
                 D5 * 3, D5, D5, G5, E5, A5) / 2

VOICE_5 = (A4 * 2 | +F4 | G4 | A4 * 2 | +F4 | G4 | A4 | KEY[A3:G4] |
           +F4 * 2 | D4 | E4 | +F4 * 2 | +F3 | G3 | A3 | B3 | A3 | G3 | A3 | +F3 | G3 | A3 |
           G3 * 2 | B3 | A3 | G3 * 2 | +F3 | E3 | +F3 | E3 | KEY[D3:B3] |
           G3 * 2 | B3 | A3 | B3 * 2 | +C4 | D4 | KEY[A3:A4] |
           +F4 * 2 | D4 | E4 | +F4 * 2 | E4 | D4 | E4 | +C4 | D4 | E4 | +F4 | E4 | D4 | +C4 |
           D4 * 2 | B3 | +C4 | D4 * 2 | D3 | E3 | +F3 | G3 | +F3 | E3 | +F3 | D4 | +C4 | D4 |
           B3 * 2 | D4 | +C4 | B3 * 2 | A3 | G3 | A3 | G3 | KEY[+F3:D4] |
           B3 * 2 | D4 | +C4 | D4 * 2 | +C4 | B3 | +C4 | D4 | E4 | D4 | +C4 | D4 | B3 | +C4).T(12) / 8

VOICE_6 = ((D4 | +C4 | B3 | D4 | D3 | D3 | D3 | E3).staccato |
           (Z / 2 | (A3 | A3 | +F3 | A3 | G3 | +F3 | G3).staccato | E4 / 2)).T(12)

VOICE_7 = (+F4 | +F3 | G3 | +F3 | E3 | E4 | +F4 | E4 | D4 | +F3 | D3 | B3 | A3 | A2 | G2 | A2 |
           B2 | B3 | +C4 | B3 | A3 | A2 | G2 | A2 | B2 | B3 | A3 | B3 | +C4 | A2 | G2 | A2 |
           D3 | D4 | E4 | D4 | +C4 | +C3 | D3 | +C3 | B2 | B3 | A3 | B3 | +C4 | +C3 | +F3 | E3 |
           D3 | D4 | E4 | G4 | +F4 | +F3 | A3 | +F4 | D4 | G4 | +F4 | G4 | E4 | A3 | G3 | A3).T(12) / 4

VOICE_8 = (+F3 | A3.x(7) | +F3.x(6) | A3 | A3 |
           G3.x(3) | D4.x(7) | B3 | B3 | A3 | A3 | E4 | +C4 |
           A3 | +F4.x(3) | E4.x(4) | D4.x(4) | A4.x(4) |
           B4.x(4) | A4.x(4) | B4.x(4) | +C5 | +C4.x(3)).T(12) / 4

VOICE_9 = (
              D4 | D3 / 2 | E3 / 2 | +F3 | D3 | +C3 | +C4 / 2 | D4 / 2 | E4 | +C4 | B3 | B2 / 2 | +C3 / 2 | D3 | B2 | +C3 | A3 / 2 | G3 / 2 | +F3 | E3 |
              D3 | G3 / 2 | +F3 / 2 | E3 | G3 | +F3 | D3 / 2 | E3 / 2 | +F3 | A3 | G3 | B3 / 2 | A3 / 2 | G3 | +F3 | E3 | A3 / 2 | G3 / 2 | +F3 | E3 |
              +F3 | D4 / 2 | +C4 / 2 | D4 | +F3 | A3 | A3 / 2 | B3 / 2 | +C4 | A3 | +F3 | D4 / 2 | E4 / 2 | +F4 | D4 | +F4 | +F4 / 2 | E4 / 2 | D4 | +C4 |
              B3 | B3 / 2 | A3 / 2 | B3 | +C4 | D4 | +F4 / 2 | E4 / 2 | D4 | +F4 | G4 | D4 / 2 | +C4 / 2 | B3 | B3 | A3 | E3 | A3 | A3).T(
    12) / 4

VOICE_10 = (A3 * 3 / 2 | A3 / 2 | D3 * 3 / 2 | A3 / 2 |
            G3 | A3 | G3 / 2 | D3 / 2 | D3 * 3 / 4 | +C3 / 4 |
            D3 / 2 | D4 / 2 | +C4 | B3 | A3 |
            D3 * 3 / 4 | (E3 / 4).staccato | +F3 | B3 | E3 * 3 / 4 | (E3 / 4).staccato).T(12)

VOICE_11 = (+F3 * 3 | +F4 | +F4 | G4 | +F4 | E4 | D4 * 3 | D4 | D4 | E4 | D4 | +C4 |
            B3 * 4 | D4 * 4 | D4 | C4 | B3 | C4 | A3 * 3 | A3 |
            A3 * 3 | A4 | A4 | B4 | A4 | G4 | +F4 * 3 | +F4 | +F4 | G4 | +F4 | E4 |
            D4 | C4 | B3 | C4 | A3 * 3 | A3 | G3 * 2 | D4 * 2 | +C4 * 3 | +C4).T(12) / 4

VOICE_12 = (D4 / 2 | D4 | +C4 | B3 | A3 | G3 | +F3 * 5 / 4 | E3 / 4 | E3 |
            +F3 / 2 | +F4 | E4 / 2 | D4 / 2 | D5 | C5 / 2 | B4 | D5 / 2 | A4 / 2 | B4 | A4 |
            A4 | A3 * 3 / 4 | G3 / 4 | +F3 | +F4 * 3 / 4 | E4 / 4 | D4 * 3 / 2 | D4 / 2 | D4 | +C3).T(
    12)  # SIX measures

VOICE_13_1 = (D4 | D3 | +C3 | +C4 | B3 | B2 | A2 | A3 |
              G3 | G4 | +F4 | +F3 | E3 | B3 | E3 | E4).T(12) / 2
VOICE_13_2 = (+F4 | +F3 | E3 | E4 | D4 | D3 | +C3 | +C4 |
              B3 | B4 | A4 | A3 | G3 * 3 / 2 | E4 / 2 | A3 | A3).T(12) / 2

VOICES = VOICE_1 | VOICE_2 | VOICE_3 | VOICE_4 | VOICE_5 | VOICE_6 | VOICE_7 | VOICE_8 | VOICE_9 | VOICE_10 | VOICE_11 | VOICE_12

PASSACAGLIA = Chord(
    (BASE.x(28) | D2 * 2) ^ 1.5,
    Z * 8 | VOICES | VOICE_13_1 | VOICE_13_2 | A4 * 2,
    Z * 16 | VOICES | VOICE_13_1 | +F5 * 2,
    Z * 24 | VOICES | D5 * 2) % 2

if __name__ == '__main__':
    PASSACAGLIA > 35
