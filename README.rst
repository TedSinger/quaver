A music composition library for Python

>>> C3.T(PFT_5)
G3
>>> (+A4).maj
{+A4, D5, F5}
>>> play(Decrescendo(2) ** Longer(2) ** Staccato ** MajorKey(D4)[D4:D5], tempo=140)

See quaver/pieces/example.py for more examples
Requires SoX `play` to automatically play, but can produce .wav files without it.