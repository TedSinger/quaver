import subprocess
import wave
import os
import tempfile
from muse.compose.constants import FRAME_RATE


def play(data, nchannels=1, sample_width=2, compression_type='NONE', compression_name='no compression'):
    f = tempfile.NamedTemporaryFile('wb', dir='/dev/shm/', delete=False)
    with wave.open(f) as w:
        w.setparams((
            nchannels,
            sample_width,
            FRAME_RATE,
            0,  # setting zero frames, should update automatically as more frames written
            compression_type,
            compression_name
        ))
        w.setnframes((0xFFFFFFFF - 36) // w.getnchannels() // w.getsampwidth())
        w.writeframesraw(data)
    subprocess.call(['play', '-t', 'wav', f.name])
    os.unlink(f.name)
