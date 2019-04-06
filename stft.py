import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.misc import toimage, imsave

fs, a = wavfile.read('./bengpendek.wav')
l = len(a)
window = 8000
kali = (l - window)/window
hsl = np.zeros((1000,1))
i = 1;
awal = 1;

print("kali", kali)

while i < kali:
    next = awal + window - 1
    b = a[awal:next]
    f = fft(b)
    f2 = np.abs(f[0:1000])
    f2T = f2.reshape(len(f2), 1)
    hsl = np.concatenate((hsl, f2T), 1)
    i = i + 1;
    awal = awal + window

#toimage(hsl).show()
imsave('./test.png', hsl)
