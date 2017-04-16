from muse.compose.notes import *
from muse.compose.keys import MinorKey

# http://www.gamemusicthemes.com/sheetmusic/gameboy/tetris/themea/Tetris_-_Theme_A_Sheet_Music_by_Gori_Fater.png

KEY = MinorKey(A4)

MELODY_1 = Stanza((B4 & E5) * 2 | +G4 & B4 | A4 & C5 | B4 & D5 | E5 / 2 | D5 / 2 | A4 & C5 | +G4 & B4) | \
           Stanza((A4 & E4) * 2 | A4 & E4 | A4 & C5 | (C5 & E5) * 2 | B4 & D5 | A4 & C5) | \
           Stanza((B4 * 3 & (+G4 | E4 | +G4)) | A4 & C5 | (B4 & D5) * 2 | (C5 & E5) * 2) | \
           Stanza((A4 & C5) * 2 | (A4 & E4) * 2 | (A4 & E4) * 4)

BASE_1 = ((E2 | E3).x(4) |
          (A2 | A3).x(4) |
          (+G2 | +G3).x(2) | (E2 | E3).x(2) |
          (A2 | A3).x(3) | B2 | C3).T(12)

MELODY_2 = Stanza(Z | (F4 & D5) * 2 | A4 & F5 | A5 * 2 & (C5 | C5 / 2 | C5 / 2) | B4 & G5 | A4 & F5) | \
           Stanza((G4 & E5) * 3 | E4 & C5 | E5 * 2 & (G4 | A4 / 2 | G4 / 2) | F4 & D5 | E4 & C5) | \
           Stanza(B4 * 2 & (+G4 | E4) | B4 & +G4 | C5 & A4 | D5 * 2 & (B4 | +G4) | E5 * 2 & (C5 | +G4)) | \
           Stanza(C5 * 2 & (A4 | E4) | (A4 & E4) * 2 | (A4 & E4) * 2 | Z * 2)

BASE_2 = Stanza(D3 | D2 | Z | D2 | Z | D2 | A2 | F2 | C2 | C3 | Z | C3 | C2 | G2 | Z | G2 |
                B2 | B3 | Z | B3 | Z | E3 | Z | +G3 | A2 | E3 | A2 | E3 | A2 * 2 | Z * 2).T(12)

MELODY_3 = (E4 & C4 | C4 & A3 | D4 & B3 | B3 & +G3 | C4 & A3 | A3 & E3 | +G3 & E3 | B3 & +G3) * 4

BASE_3_4 = ((A3 | E3).x(4) | (+G3 | E3).x(4)).x(4)
MELODY_4 = (E4 & C4 | C4 & A3 | D4 & B3 | B3 & +G3 |
            (A3 & C4 | E4 & C4) / 2 | C4 & A4 | (E4 & +G4) * 2) * 4

THEME_A = (MELODY_1 | MELODY_2 | MELODY_3 | MELODY_4) & (BASE_1 | BASE_2 | BASE_3_4)

if __name__ == '__main__':
    THEME_A > 240
