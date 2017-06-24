_HALF_STEP_INTERVAL = 2 ** (1 / 12.)

OCTAVE = 12
MAJ_7 = 11
MIN_7 = 10
MAJ_6 = 9
MIN_6 = 8
PFT_5 = 7  # 2**(7/12) is very close to 3/2
PFT_4 = 5  # 2**(5/12) is very close to 4/3
MAJ_3 = 4
MIN_3 = 3

A440 = 440

_C4_FREQ = A440 / _HALF_STEP_INTERVAL ** 9
FRAME_RATE = (2 * 3 * 5 * 7) ** 2  # 44100