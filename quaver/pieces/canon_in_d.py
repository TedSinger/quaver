from quaver.compose import *
from quaver.pieces.demo import trill

BASE = Stanza(D3, A2, B2, +F2, G2, D2, G2, A2)

_PIZZ = Stanza(D3.maj, A2.maj, B2.min, +F2.min, G2.maj, D2.maj, G2.maj, A2.maj)
PIZZ = Stanza(*[(Z | (c.splayed * 3)) for c in _PIZZ]).T(12).staccato / 4

BARS_2_5 = Stanza(+F4, E4, D4, +C4, B3, A3, B3, +C4,
                  D4, +C4, B3, A3, G3, +F3, G3, E3).T(12)

BARS_6_9 = Stanza(D4, +F4, A4, G4, +F4, D4, +F4, E4,
                  D4, B3, D4, A4, G4, B4, A4, G4,
                  +F4, D4, E4, +C5, D5, +F5, A5, A4,
                  B4, G4, A4, +F4, D4, D5, trill(D5 * 3 / 2, 2), +C5 / 2) / 2

BARS_10_13 = Stanza(D5, +C5, D5, D4, +C4, A4, E4, +F4,
                    D4, D5, +C5, B4, +C5, +F5, A5, B5,
                    G5, +F5, E5, G5, +F5, E5, D5, +C5,
                    B4, A4, G4, +F4, E4, G4, +F4, E4,
                    D4, E4, +F4, G4, A4, E4, A4, G4,
                    +F4, B4, A4, G4, A4, G4, +F4, E4,
                    D4, B3, B4, +C5, D5, +C5, B4, A4,
                    G4, +F4, E4, B4, A4, B4, A4, G4) / 4

BARS_14_17 = Stanza(+F4, +F5, E5 * 2, Z, D5, +F5 * 2,
                    B5 * 2, A5 * 2, B5 * 2, +C6 * 2,
                    D6, D5, +C5 * 2, Z, B4, D5 * 2,
                    D5 * 3, D5, D5, G5, E5, A5) / 2

BARS_18_21 = (A4 * 2 | +F4 | G4 | A4 * 2 | +F4 | G4 | A4 | DMaj[A3:G4] |
              +F4 * 2 | D4 | E4 | +F4 * 2 | +F3 | G3 | A3 | B3 | A3 | G3 | A3 | +F3 | G3 | A3 |
              G3 * 2 | B3 | A3 | G3 * 2 | +F3 | E3 | +F3 | E3 | DMaj[D3:B3] |
              G3 * 2 | B3 | A3 | B3 * 2 | +C4 | D4 | DMaj[A3:A4] |
              +F4 * 2 | D4 | E4 | +F4 * 2 | E4 | D4 | E4 | +C4 | D4 | E4 | +F4 | E4 | D4 | +C4 |
              D4 * 2 | B3 | +C4 | D4 * 2 | D3 | E3 | +F3 | G3 | +F3 | E3 | +F3 | D4 | +C4 | D4 |
              B3 * 2 | D4 | +C4 | B3 * 2 | A3 | G3 | A3 | G3 | DMaj[+F3:D4] |
              B3 * 2 | D4 | +C4 | D4 * 2 | +C4 | B3 | +C4 | D4 | E4 | D4 | +C4 | D4 | B3 | +C4).T(12) / 8

BARS_22_25 = ((D5 | +C5 | B4 | D5 | D4 | D4 | D4 | E4).staccato |
              (Z / 2 | (A4 | A4 | +F4 | A4 | G4 | +F4 | G4).staccato | E5 / 2))

BARS_26_29 = (+F4 | +F3 | G3 | +F3 | E3 | E4 | +F4 | E4 | D4 | +F3 | D3 | B3 | A3 | A2 | G2 | A2 |
              B2 | B3 | +C4 | B3 | A3 | A2 | G2 | A2 | B2 | B3 | A3 | B3 | +C4 | A2 | G2 | A2 |
              D3 | D4 | E4 | D4 | +C4 | +C3 | D3 | +C3 | B2 | B3 | A3 | B3 | +C4 | +C3 | +F3 | E3 |
              D3 | D4 | E4 | G4 | +F4 | +F3 | A3 | +F4 | D4 | G4 | +F4 | G4 | E4 | A3 | G3 | A3).T(12) / 4

BARS_30_33 = (+F3 | A3.x(7) | +F3.x(6) | A3 | A3 |
              G3.x(3) | D4.x(7) | B3 | B3 | A3 | A3 | E4 | +C4 |
              A3 | +F4.x(3) | E4.x(4) | D4.x(4) | A4.x(4) |
              B4.x(4) | A4.x(4) | B4.x(4) | +C5 | +C4.x(3)).T(12) / 4

BARS_34_37 = (D4 | D3 / 2 | E3 / 2 | +F3 | D3 | +C3 | +C4 / 2 | D4 / 2 | E4 | +C4 |
              B3 | B2 / 2 | +C3 / 2 | D3 | B2 | +C3 | A3 / 2 | G3 / 2 | +F3 | E3 |
              D3 | G3 / 2 | +F3 / 2 | E3 | G3 | +F3 | D3 / 2 | E3 / 2 | +F3 | A3 |
              G3 | B3 / 2 | A3 / 2 | G3 | +F3 | E3 | A3 / 2 | G3 / 2 | +F3 | E3 |
              +F3 | D4 / 2 | +C4 / 2 | D4 | +F3 | A3 | A3 / 2 | B3 / 2 | +C4 | A3 |
              +F3 | D4 / 2 | E4 / 2 | +F4 | D4 | +F4 | +F4 / 2 | E4 / 2 | D4 | +C4 |
              B3 | B3 / 2 | A3 / 2 | B3 | +C4 | D4 | +F4 / 2 | E4 / 2 | D4 | +F4 |
              G4 | D4 / 2 | +C4 / 2 | B3 | B3 | A3 | E3 | A3 | A3).T(12) / 4

BARS_38_41 = (A3 * 3 / 2 | A3 / 2 | D3 * 3 / 2 | A3 / 2 |
              G3 | A3 | G3 / 2 | D3 / 2 | D3 * 3 / 4 | +C3 / 4 |
              D3 / 2 | D4 / 2 | +C4 | B3 | A3 |
              D3 * 3 / 4 | E3 / 8 | Z / 8 | +F3 | B3 | E3 * 3 / 4 | E3 / 8 | Z / 8).T(12)

BARS_42_45 = (+F3 * 3 | +F4 | +F4 | G4 | +F4 | E4 | D4 * 3 | D4 | D4 | E4 | D4 | +C4 |
              B3 * 4 | D4 * 4 | D4 | C4 | B3 | C4 | A3 * 3 | A3 |
              A3 * 3 | A4 | A4 | B4 | A4 | G4 | +F4 * 3 | +F4 | +F4 | G4 | +F4 | E4 |
              D4 | C4 | B3 | C4 | A3 * 3 | A3 | G3 * 2 | D4 * 2 | +C4 * 3 | +C4).T(12) / 4

BARS_46_51 = (D5 / 2 | D5 | +C5 | B4 | A4 | G4 | +F4 * 5 / 4 | E4 / 4 | E4 |
              +F4 / 2 | +F5 | E5 / 2 | D5 / 2 | D6 | C6 / 2 | B5 | D6 / 2 | A5 / 2 | B5 | A5 |
              A5 | A4 * 3 / 4 | G4 / 4 | +F4 | +F5 * 3 / 4 | E5 / 4 | D5 * 3 / 2 | D5 / 2 | D5 | +C4)  # SIX measures

BARS_52_53 = (D4 | D3 | +C3 | +C4 | B3 | B2 | A2 | A3 |
              G3 | G4 | +F4 | +F3 | E3 | B3 | E3 | E4).T(12) / 2

BARS_54_55 = (+F4 | +F3 | E3 | E4 | D4 | D3 | +C3 | +C4 |
              B3 | B4 | A4 | A3 | G3 * 3 / 2 | E4 / 2 | A3 | A3).T(12) / 2

COMMON_VOICES = BARS_2_5 | BARS_6_9 | BARS_10_13 | BARS_14_17 | BARS_18_21 | BARS_22_25 | \
                BARS_26_29 | BARS_30_33 | BARS_34_37 | BARS_38_41 | BARS_42_45 | BARS_46_51

PASSACAGLIA = Chord(
    (BASE.x(28) | D2 * 3 / 2),
    PIZZ.x(28),
    (Z * 8 | COMMON_VOICES | BARS_52_53 | BARS_54_55 | A4 * 3 / 2),
    (Z * 16 | COMMON_VOICES | BARS_52_53 | +F5 * 3 / 2),
    (Z * 24 | COMMON_VOICES | D5 * 3 / 2)) % 2

if __name__ == '__main__':
    PASSACAGLIA > 35
