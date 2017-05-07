from quaver.compose import *

if False:
    C3  # a C quarter note
    +C3  # a C sharp
    -C3  # a C flat
    C3.x(4) == Stanza(C3, C3, C3, C3)  # repeated four times
    C3 * 2  # a half note
    C3 / 2  # an eighth note
    C3 ^ 2  # **LOUDER**
    C3 % 2  # ..softer..
    C3.T(7) == G3  # Transposed up seven half-steps (a perfect fifth)
    Z  # A quarter rest
    Z.T(7) % 2 == Z  # Unchanged - rests are not affected by pitch or dynamics...
    Z / 2  # ...but tempo changes still work
    A4 & +C5 & E5 == Chord(A4, +C5, E5)  # Three notes to be played together
    A4 | +C5 | E5 == Stanza(A4, +C5, E5)  # Three notes to be played sequentially
    A4.maj == Chord(A4, +C5, E5)  # Simple chords have shortcuts
    Stanza(A4.maj, D5.min)  # You can put Stanzas in Chords, or Chords in Stanzas, nested as deeply as you want
    ((A4.maj | D5.min).x(4).T(-5) / 2) % 2  # Chords and Stanzas apply operations to ALL of their contents

    A4.maj.to_sound(60).to_wav('~/amajchord.wav')  # Create a wav file at 60 beats per minute
    A4.maj > 60  # Create a tempfile and play it immediately (Linux only)


# It's all regular Python code. You can write your own functions!
def trill(note: Note, n: int):
    atempo = note._with('duration', FRAME_RATE / 16)
    s = Stanza(atempo, atempo.T(n))
    return atempo * 3 | atempo.T(n) * 2 | \
           s.x(round((note.duration - atempo.duration * 6) / (2 * atempo.duration))) | \
           atempo
