from quaver.compose import *
from quaver.pieces.example import trill

BASE = (D3, A2, B2, +F2, G2, D2, G2, A2)

_PIZZ = (D3.maj, A2.maj, B2.min, (+F2).min, G2.maj, D2.maj, G2.maj, A2.maj)
PIZZ = T(12)(Staccato(SIXTEENTH(tuple((Z,) + tuple(sorted(c)) for c in _PIZZ))))

BARS_2_5 = T(12)((+F4, E4, D4, +C4, B3, A3, B3, +C4,
                  D4, +C4, B3, A3, G3, +F3, G3, E3))

BARS_6_9 = (EIGHTH((D4, +F4, A4, G4, +F4, D4, +F4, E4,
                    D4, B3, D4, A4, G4, B4, A4, G4,
                    +F4, D4, E4, +C5, D5, +F5, A5, A4,
                    B4, G4, A4, +F4, D4, D5))) + \
           trill(D5._3_16, 2) + (+C5._16,)

BARS_10_13 = SIXTEENTH((D5, +C5, D5, D4, +C4, A4, E4, +F4,
                        D4, D5, +C5, B4, +C5, +F5, A5, B5,
                        G5, +F5, E5, G5, +F5, E5, D5, +C5,
                        B4, A4, G4, +F4, E4, G4, +F4, E4,
                        D4, E4, +F4, G4, A4, E4, A4, G4,
                        +F4, B4, A4, G4, A4, G4, +F4, E4,
                        D4, B3, B4, +C5, D5, +C5, B4, A4,
                        G4, +F4, E4, B4, A4, B4, A4, G4))

BARS_14_17 = Shorter(2)(
    (+F4, +F5, E5._2, Z, D5, +F5._2,
     B5._2, A5._2, B5._2, +C6._2,
     D6, D5, +C5._2, Z, B4, D5._2,
     D5._3_4, D5, D5, G5, E5, A5))

BARS_18_21 = T(12)(Shorter(8)(
    (A4._2, +F4, G4, A4._2, +F4, G4, A4, DMaj[A3:G4],
     +F4._2, D4, E4, +F4._2, +F3, G3, A3, B3, A3, G3, A3, +F3, G3, A3,
     G3._2, B3, A3, G3._2, +F3, E3, +F3, E3, DMaj[D3:B3],
     G3._2, B3, A3, B3._2, +C4, D4, DMaj[A3:A4],
     +F4._2, D4, E4, +F4._2, E4, D4, E4, +C4, D4, E4, +F4, E4, D4, +C4,
     D4._2, B3, +C4, D4._2, D3, E3, +F3, G3, +F3, E3, +F3, D4, +C4, D4,
     B3._2, D4, +C4, B3._2, A3, G3, A3, G3, DMaj[+F3:D4],
     B3._2, D4, +C4, D4._2, +C4, B3, +C4, D4, E4, D4, +C4, D4, B3, +C4)))

BARS_22_25 = Staccato((D5, +C5, B4, D5, D4, D4, D4, E4)) + \
             (Z._8,) + Staccato((A4, A4, +F4, A4, G4, +F4, G4)) + (E5._8,)

BARS_26_29 = T(12)(Shorter(4)(
    (+F4, +F3, G3, +F3, E3, E4, +F4, E4, D4, +F3, D3, B3, A3, A2, G2, A2,
     B2, B3, +C4, B3, A3, A2, G2, A2, B2, B3, A3, B3, +C4, A2, G2, A2,
     D3, D4, E4, D4, +C4, +C3, D3, +C3, B2, B3, A3, B3, +C4, +C3, +F3, E3,
     D3, D4, E4, G4, +F4, +F3, A3, +F4, D4, G4, +F4, G4, E4, A3, G3, A3)))

BARS_30_33 = T(12)(Shorter(4)(
    (+F3, A3 * 7, +F3 * 6, A3, A3,
     G3 * 3, D4 * 7, B3, B3, A3, A3, E4, +C4,
     A3, +F4 * 3, E4 * 4, D4 * 4, A4 * 4,
     B4 * 4, A4 * 4, B4 * 4, +C5, +C4 * 3)))

BARS_34_37 = T(12)(Shorter(4)(
    (D4, D3._8, E3._8, +F3, D3, +C3, +C4._8, D4._8, E4, +C4,
     B3, B2._8, +C3._8, D3, B2, +C3, A3._8, G3._8, +F3, E3,
     D3, G3._8, +F3._8, E3, G3, +F3, D3._8, E3._8, +F3, A3,
     G3, B3._8, A3._8, G3, +F3, E3, A3._8, G3._8, +F3, E3,
     +F3, D4._8, +C4._8, D4, +F3, A3, A3._8, B3._8, +C4, A3,
     +F3, D4._8, E4._8, +F4, D4, +F4, +F4._8, E4._8, D4, +C4,
     B3, B3._8, A3._8, B3, +C4, D4, +F4._8, E4._8, D4, +F4,
     G4, D4._8, +C4._8, B3, B3, A3, E3, A3, A3)))

BARS_38_41 = T(12)(
    (A3._3_8, A3._8, D3._3_8, A3._8,
     G3, A3, G3._8, D3._8, D3._3_16, +C3._16,
     D3._8, D4._8, +C4, B3, A3,
     D3._3_16, E3._32, Z._32, +F3, B3, E3._3_16, E3._32, Z._32))

BARS_42_45 = T(12)(Shorter(4)(
    (+F3._3_4, +F4, +F4, G4, +F4, E4, D4._3_4, D4, D4, E4, D4, +C4,
     B3._1, D4._1, D4, C4, B3, C4, A3._3_4, A3,
     A3._3_4, A4, A4, B4, A4, G4, +F4._3_4, +F4, +F4, G4, +F4, E4,
     D4, C4, B3, C4, A3._3_4, A3, G3._2, D4._2, +C4._3_4, +C4)))

BARS_46_51 = (D5._8, D5, +C5, B4, A4, G4, +F4._5_16, E4._16, E4,
              +F4._8, +F5, E5._8, D5._8, D6, C6._8, B5, D6._8, A5._8, B5, A5,
              A5, A4._3_16, G4._16, +F4, +F5._3_16, E5._16, D5._3_8, D5._8, D5, +C4)  # SIX measures

BARS_52_53 = T(12)(Shorter(2)(
    (D4, D3, +C3, +C4, B3, B2, A2, A3,
     G3, G4, +F4, +F3, E3, B3, E3, E4)))

BARS_54_55 = T(12)(Shorter(2)(
    (+F4, +F3, E3, E4, D4, D3, +C3, +C4,
     B3, B4, A4, A3, G3._3_8, E4._8, A3, A3)))

COMMON_VOICES = (BARS_2_5, BARS_6_9, BARS_10_13, BARS_14_17, BARS_18_21, BARS_22_25,
                 BARS_26_29, BARS_30_33, BARS_34_37, BARS_38_41, BARS_42_45, BARS_46_51)

PASSACAGLIA = {
    (BASE * 28, D2._3_8),
    PIZZ * 28,
    Louder(2)((Z * 8, COMMON_VOICES, BARS_52_53, BARS_54_55, A4._3_8)),
    (Z * 16, COMMON_VOICES, BARS_52_53, +F5._3_8),
    (Z * 24, COMMON_VOICES, D5._3_8)}

if __name__ == '__main__':
    play(PASSACAGLIA, tempo=35)
