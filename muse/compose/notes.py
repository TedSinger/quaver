from muse.compose.sounds import Note, Silence
from muse.compose.constants import OCTAVE, A440
from muse.compose.structure import Chord, Stanza


A4 = Note(A440)
def _generate_note_defns():
    s = ''
    for i in range(-OCTAVE * 4, OCTAVE * 2):
        if '.' not in str(A4.T(i)):
            s += str(A4.T(i)) + ' = A4.T(%s)\n' % i
    return s

Z = Silence()
A0 = A4.T(-48)
B0 = A4.T(-46)
C1 = A4.T(-45)
D1 = A4.T(-43)
E1 = A4.T(-41)
F1 = A4.T(-40)
G1 = A4.T(-38)
A1 = A4.T(-36)
B1 = A4.T(-34)
C2 = A4.T(-33)
D2 = A4.T(-31)
E2 = A4.T(-29)
F2 = A4.T(-28)
G2 = A4.T(-26)
A2 = A4.T(-24)
B2 = A4.T(-22)
C3 = A4.T(-21)
D3 = A4.T(-19)
E3 = A4.T(-17)
F3 = A4.T(-16)
G3 = A4.T(-14)
A3 = A4.T(-12)
B3 = A4.T(-10)
C4 = A4.T(-9)
D4 = A4.T(-7)
E4 = A4.T(-5)
F4 = A4.T(-4)
G4 = A4.T(-2)
A4 = A4.T(0)
B4 = A4.T(2)
C5 = A4.T(3)
D5 = A4.T(5)
E5 = A4.T(7)
F5 = A4.T(8)
G5 = A4.T(10)
A5 = A4.T(12)
B5 = A4.T(14)
C6 = A4.T(15)
D6 = A4.T(17)
E6 = A4.T(19)
F6 = A4.T(20)
G6 = A4.T(22)