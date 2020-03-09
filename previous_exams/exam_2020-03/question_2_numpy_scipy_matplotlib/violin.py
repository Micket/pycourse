"""

Tasks

1. Read the file using scipy.io.wavefile
2. Plot the real time wave form vs. time [seconds].
3. Comput the frequency power spectra using numpy.fft.fft and numpy.fft.fftfreq
4. Plot the power spectra vs. frequency [Hertz] in the range [0, 3000] Hz.

5. What is the base frequency of the tone the violin is playing?
   A: 261.64 Hz

6. Write a function that converts from frequency to musical notes

f_A4 = 440
f_C0 = f_A4 * 2^{-4.75}
h = round( 12 * log_2 ( f / f_C0 ) )
octave = h / 12
note_idx = h % 12
notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

7. What note is the violin playing?
   A: C4

"""

import numpy as np
import matplotlib.pyplot as plt

from scipy.io import wavfile

rate, sound = wavfile.read('violin.wav')
print(rate, sound.shape)

t = np.arange(len(sound)) / rate
power_spectra = np.abs(np.fft.fft(sound))
frequency = np.fft.fftfreq(len(power_spectra), d=1./rate)

sidx = np.argsort(frequency)

frequency = frequency[sidx]
power_spectra = power_spectra[sidx]

midx = np.argmax(power_spectra)
base_freq = np.abs(frequency[midx])
print('base freq =', base_freq)

def pitch(frequency):
    """ Given a tone frequency in Hertz return the notation 
    of the correspnding musical note. """
    frequency_A4 = 440
    frequency_C0 = frequency_A4 * 2**-4.75
    h = np.rint(12*np.log2(frequency / frequency_C0)).astype(int)
    
    octave, note_idx = h // 12, h % 12
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[note_idx] + str(octave)

tone = pitch(base_freq)
print('tone =', tone)

# --

plt.figure(figsize=(10, 3))
subp = [1, 2, 1]
plt.subplot(*subp); subp[-1] += 1
plt.plot(t, sound)
plt.ylabel('Amplitude [arb. units]')
plt.xlabel('Time [seconds]')

plt.subplot(*subp); subp[-1] += 1
plt.plot(frequency, power_spectra)
plt.ylabel('Power spectra [arb. units]')
plt.xlabel('Frequency [Hertz]')
plt.xlim([0, 3000])

plt.tight_layout()
plt.savefig('figure_violin.png', dpi=300)
plt.show()


