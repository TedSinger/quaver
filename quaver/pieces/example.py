from quaver.compose import *

if False:
    C3  # a C quarter note
    +C3  # a C sharp
    -C3  # a C flat
    C3 * 4 == (C3, C3, C3, C3)  # repeated four times
    C3._2  # a half note
    C3._8  # an eighth note
    C3._3_8 # a dotted quarter
    Louder(2) ** C3  # **Louder**
    Softer(2) ** C3  # ..Softer..
    T(7) ** C3 == G3  # Transposed up seven half-steps (a perfect fifth)
    Z  # A quarter rest
    Louder(2) ** T(7) ** Z == Z  # Unchanged - rests are not affected by pitch or dynamics...
    Z._2  # ...but tempo changes still work
    {A4, +C5, E5}  # A chord - three notes to be played together
    (A4, +C5, E5)  # A stanza - three notes to be played sequentially
    A4.maj == {A4, +C5, E5}  # Simple chords have shortcuts
    (A4.maj, D5.min)  # You can put stanzas in chords, or chords in stanzas, nested as deeply as you want
    Shorter(2) ** Softer(2) ** T(-5) ** (A4.maj, D5.min)  # Chords and stanzas apply operations to ALL of their contents

    to_wav(A4.maj, filename='~/amajchord.wav', tempo=60)  # Create a wav file at 60 beats per minute
    play(A4.maj, tempo=60)  # Create a tempfile and play it immediately, at 60 bpm (Linux only)


# It's all regular Python code. You can write your own functions!
def trill(note: Note, n: int):
    note2 = T(n) ** note
    pair = (note, note2)
    return ((note.len / 8) ( pair)) + ((note.len / 16) ( pair)) * 4 + (note.len / 4) ((note,))
