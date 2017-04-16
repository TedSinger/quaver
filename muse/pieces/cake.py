from muse.compose.notes import *

a = Stanza(A3, D4, F4.s, D4)
b = Stanza(B3, D4, F4.s, D4)
c = Stanza(B3, E4, G4, E4)
d = Stanza(A3, E4, G4, C4.s)
CAKE_BASE = (a | b).x(4) | (c | c | d | d) | (a | b).x(2)
CAKE_FROSTING = Stanza(G4, F4.s, E4, E4, F4.s, Z * 3,  # a
                       Z * 7, A3,  # b a
                       G4, F4.s, E4, E4, Z / 2, F4.s * 3 / 2, Z * 2,  # ba
                       D4, Z, E4, A3 * 2, Z * 3,  # ba
                       Z * 3, A3, E4 * 2, F4.s,  # bc
                       G4 * 2, E4 * 2, C4.s * 2, D4, E4 * 2, A3.staccato,  # cd
                       A3 * 2, F4.s * 2, Z * 4)  # d
FULL = (CAKE_FROSTING & (Z * 4 | CAKE_BASE.staccato) / 4)

if __name__ == '__main__':
    FULL > Z
