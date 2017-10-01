from quaver.compose import *

# http://www.gamemusicthemes.com/sheetmusic/gameboy/tetris/themea/Tetris_-_Theme_A_Sheet_Music_by_Gori_Fater.png

KEY = MinorKey(A4)

MELODY_1 = ({B4._2, E5._2}, {+G4, B4}, {A4, C5}, {B4, D5}, E5._8, D5._8, {A4, C5}, {+G4, B4}) + \
           ({A4._2, E4._2}, {A4, E4}, {A4, C5}, {C5._2, E5._2}, {B4, D5}, {A4, C5}) + \
           ({B4._3_4, (+G4, E4, +G4)}, {A4, C5}, {B4._2, D5._2}, {C5._2, E5._2}) + \
           ({A4._2, C5._2}, {A4._2, E4._2}, {A4._1, E4._1})

BASE_1 = T(12) ** ((E2, E3) * 4 +
                   (A2, A3) * 4 +
                   (+G2, +G3) * 2 + (E2, E3) * 2 +
                   (A2, A3) * 3 + (B2, C3))

MELODY_2 = (Z, {F4._2, D5._2}, {A4, F5}, {A5._2, (C5, C5._8, C5._8)}, {B4, G5}, {A4, F5}) + \
           ({G4._3_4, E5._3_4}, {E4, C5}, {E5._2, (G4, A4._8, G4._8)}, {F4, D5}, {E4, C5}) + \
           ({B4._2, (+G4, E4)}, {B4, +G4}, {C5, A4}, {D5._2, (B4, +G4)}, {E5._2, (C5, +G4)}) + \
           ({C5._2, (A4, E4)}, {A4._2, E4._2}, {A4._2, E4._2}, Z._2)

BASE_2 = T(12) ** (D3, D2, Z, D2, Z, D2, A2, F2, C2, C3, Z, C3, C2, G2, Z, G2,
                   B2, B3, Z, B3, Z, E3, Z, +G3, A2, E3, A2, E3, A2._2, Z._2)

MELODY_3 = Longer(4) ** ({E4, C4}, {C4, A3}, {D4, B3}, {B3, +G3}, {C4, A3}, {A3, E3}, {+G3, E3}, {B3, +G3})

BASE_3_4 = (((A3, E3) * 4) + ((+G3, E3) * 4)) * 4
MELODY_4 = Longer(4) ** ({E4, C4}, {C4, A3}, {D4, B3}, {B3, +G3},
                        ({A3._8, C4._8}, {E4._8, C4._8}), {C4, A4}, {E4._2, +G4._2})

THEME_A = {'m': (MELODY_1, MELODY_2) * 2 + (MELODY_3, MELODY_4) * 2,
           'b': (BASE_1, BASE_2) * 2 + BASE_3_4 * 2}

if __name__ == '__main__':
    play(THEME_A, tempo=240)
