import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.misc import toimage, imsave

fs, a = wavfile.read('./demung/1-3.wav')
l = len(a)
window = 8000
hop = 2000
kali = (l - window - hop)/hop
hsl = np.zeros((1000,1))
i = 1;
awal = 1;

while i < kali:
    next = awal + window - 1
    b = a[awal:next]
    f = fft(b)
    f2 = np.abs(f[0:1000])
    f2T = f2.reshape(len(f2), 1)
    hsl = np.concatenate((hsl, f2T), 1)
    i = i + 1;
    awal = awal + hop

print(hsl.max())
'''
result = np.where(hsl == np.amax(hsl))
listOfCoordinates = list(zip(result[0], result[1]))

for cord in listOfCoordinates:
    print(cord)
'''
toimage(hsl).show()
#imsave('./11.png', hsl)
