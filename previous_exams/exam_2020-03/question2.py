""" Question 2 """


# Part A


import numpy as np

def pitch(frequency):
    """ Given a tone frequency in Hertz return the notation 
    of the correspnding musical note. """
    frequency_A4 = 440
    frequency_C0 = frequency_A4 * 2**-4.75

    # NumPy
    h = np.rint(12*np.log2(frequency / frequency_C0)).astype(int)

    # STD Python
    from math import log2
    h_ref = round(12 * log2( frequency / frequency_C0 ))

    np.testing.assert_almost_equal(h, h_ref)
    
    octave, note_idx = h // 12, h % 12
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return notes[note_idx] + str(octave)

frequency = 440.
print(pitch(frequency), '=', frequency, 'Hz')


# Part B


import matplotlib.pyplot as plt

from scipy.io import wavfile

rate, sound = wavfile.read('piano.wav')
t = np.arange(len(sound)) / rate

plt.figure(figsize=(8, 3))
plt.plot(t, sound)
plt.ylabel('Amplitude [arb. units]')
plt.xlabel('Time [seconds]')
plt.tight_layout()
plt.savefig('figure_q2_time.png', dpi=300)


# Part C


power_spectra = np.abs(np.fft.fft(sound))
frequency = np.fft.fftfreq(len(power_spectra), d=1./rate)

midx = np.argmax(power_spectra)
base_frequency = np.abs(frequency[midx])
note = pitch(base_frequency)

print('The frequency of the violin sound is', base_frequency, 'which correspond to the note', note)

plt.figure(figsize=(8, 3))
plt.plot(frequency, power_spectra)
plt.ylabel('Power spectra [arb. units]')
plt.xlabel('Frequency [Hertz]')
plt.xlim([0, 3000])
plt.tight_layout()
plt.savefig('figure_q2_frequency.png', dpi=300)

plt.show()
