---
header-includes:
        - \usepackage[left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 2: Musical analysis (6p)

You are prototyping an Python based musical tuning program for a well known Violin manufacturer. The company has sent over a test recording of a violin, see the file `violin.wav`, and your boss has given you the task to implement two parts of the project.

**Note:** You `must` use NumPy types to store any sequence data in this task! Also, you `must not` use any loops in this task!

Part A (2p)
-------------

**Task:** Implement a function `pitch` that takes a floating point value `frequency`, in the unit of Hertz (Hz), as input and returns a text string with the corresponding musical note and octave. Remember to document the function.

**Example:** The frequency 440 Hz corresponds to A4, were A denotes the tone and 4 denotes the octave. Here is an example usage of the function `pitch`
```python
freqency = 440. # unit Hertz
print(pitch(frequency), '=', frequency, 'Hz')
```
should give the result
```
A4 = 440.0 Hz
```

**Background:** Converting a frequency $f$ in Hertz to a note $n$ and octave $o$ can be done this way:

* Compute $h = 12 \cdot \log_2 ( f / f_{C0})$
  * Here $f_{C0}$ is the frequency for the note C0 which is given by $f_{C0} = f_{A4} \cdot 2^{-4.75}$
  * $f_{A4} = 440\,$Hz is the base frequency
* Let $[h]$ denote the integer closest to $h$
* The octave $o$ is given by the result of the integer division of $[h]$ with $12$
* The index of the note $n$ is given by the remainder of the integer division above
* To map the note index $n$ to actual notes use the list of notes: [C, C#, D, D#, E, F, F#, G, G#, A, A#, B]

**Hint:** Use the standard `round` function and the `log2` function from the `math` module of the Python standard library, or the equivalent NumPy functions.

Part B (1p)
-----------

**Task:** Write code that reads the sound file `violin.wav` and plots the sound amplitude data as a function of time, using *seconds* as the time unit (i.e. for the x-axis). Make sure to add a title as well as x- and y-labels including information on units.

**Hints:** 

* To read the file use a suitable method from the `scipy.io` module, see the SciPy documentation. 
* The sound data has two components, 
  * the amplitude $A(t)$, as a function of time $t$, and 
  * the sample rate $R$, given in the unit of Hz, determining the number of amplitude data points per second.
* The time $t_i$ of the data point with index $i$ is given by $t_i = i/R$.
* For an example plot see Fig. 1.

\newpage

![Example plot of the sound amplitude as a function of time (of a different sound than `violin.wav`).](figure_q2_time.png){ width=95% }

Part C (3p)
-----------

**Task:** Determine the dominating frequency in the sound file `violin.wav` and use your `pitch` function to compute the corresponding musical note. Do this by *computing* and *plotting* the amplitude of the sound as a function of frequency (instead of time). Make sure to add a title as well as x- and y-labels including information on units. Use a suitable NumPy function to find the maximum amplitude in frequency and use this frequency as input to your `pitch` function, to compute and print the corresponding musical note.

**Hints:**

- The amplitude of the sound $A(v)$ as a function of frequency $v$ can be computed by taking the absolute value of the Fourier transform $\mathcal{F}\{ \cdot \}$ of the amplitude as a function of time $A(t)$, i.e. $A(v) = | \mathcal{F}\{ A(t) \} |$.
- To compute $\mathcal{F}\{A(t)\}$ use the `numpy.fft.fft` function, and to compute $v$ use the `numpy.fft.fftfreq` function, see the NumPy documentation.
* For an example plot see Fig. 2.

![Example plot of the sound amplitude as a function of frequency (of a different sound than `violin.wav`). The frequency of the tone in this example is 440 Hz, which corresponds to the note A4, as can be seen in the plot from the location in frequency of the largest peak.](figure_q2_frequency.png){ width=95% }

