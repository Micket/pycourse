"""
DAT171 Object-oriented programming in Python
Computer Assignment 1
Step 1: Example Solution

Author: Hugo Strand, hugo.strand@gmail.com
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt

def parse_line(line):
    return [float(value) for value in line.replace(';', ',').split(',')]


# -- Read file
filename = 'ca1_step1_input_data.txt'
print('--> Loading:', filename)
with open(filename, 'r') as fd:
    lines = fd.readlines()

# -- Parse header
header, lines = lines[1], lines[2:]
time_steps, time_step, radius, v_variance, N_particles = parse_line(header)
time_steps, N_particles = int(time_steps), int(N_particles)

# -- Find block of text for each time step and parse its lines
block_line_idxs = [idx for idx, line in enumerate(lines) if 'time_step' in line]
blocks_lines = [lines[idx + 2:idx + 2 + N_particles] for idx in block_line_idxs]
data = [[parse_line(line) for line in block_lines] for block_lines in blocks_lines]

print(len(data), len(data[0]), len(data[0][0]), type(data[0][0][0]))
print('block_line_idxs =', block_line_idxs)

# -- Transform into NumPy array
data = np.array(data)
assert(data.shape == (time_steps, N_particles, 4))

print(type(data))
print(data.dtype)
print(data.shape)

# -- Separate positions and velocities
# time_steps has rank 3
# the first index is the time step (t)
# the second index the particle (p)
# the third index the 2D positions and velocities (x, y and v_x, v_y)
# using (i) to label the cartesian index (x, y)
R = np.swapaxes(data[..., :2], 1, 2)
V = np.swapaxes(data[..., 2:], 1, 2)

print(R.shape)
print(V.shape)

# -- Plot the positions of the first time step
r = R[0]  # zero:th time step
x = r[0, :]
y = r[1, :]
plt.figure()
plt.scatter(x, y)
plt.axis('square')
plt.xlim([-1, 1])
plt.ylim([-1, 1])
filename = 'ca1_step1_figure1.svg'
print('--> Plotting:', filename)
plt.savefig(filename, bbox_inches='tight')

# -- Store to pkl
filename = 'ca1_step1_output_data.pkl'
print('--> Storing:', filename)
with open(filename, 'wb') as fd:
    pickle.dump((R, V, radius, time_step, v_variance), fd)
