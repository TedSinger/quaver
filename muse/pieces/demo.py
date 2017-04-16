from muse.compose import *

C3  # a C quarter note
+C3  # a C sharp
-C3  # a C flat
C3.x(4)  # repeated four times
C3 * 2  # a half note
C3 / 2  # an eighth note
C3 ^ 2  # **LOUDER**
C3 % 2  # ..softer..
C3.T(7)  # Transposed up seven half-steps (a perfect fifth)
Z  # a quarter rest
Chord(A4, +C5, E5)  # Three notes to be played together
A4 & +C5 & E5  # Written differently
Stanza(A4, +C5, E5)  # Three notes to be played sequentially
A4 | +C5 | E5  # Written differently
A4.maj  # Chord(A4, +C5, E5) - Simple chords have shortcuts
Stanza(A4.maj, D4.maj)  # You can put Stanzas in Chords, or Chords in Stanzas, nested as deeply as you want
((A4.maj | D4.maj).x(4).T(-5) / 2) % 2  # Chords and Stanzas apply operations to ALL of their contents
Z.T(7) % 2  # unchanged - rests are not affected by pitch or dynamics
Z / 2  # but tempo changes still work

A4.maj.to_sound(60).to_wav('/home/ted/amajchord.wav')  # create a wav file at 60 beats per minute
A4.maj > 60  # create a tempfile and play it immediatey
