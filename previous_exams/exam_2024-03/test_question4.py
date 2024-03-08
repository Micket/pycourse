import math
import numpy as np

weights = np.array([[1, 2, 0, 1], [3, 1, 1, 0], [4, 2, 1, 1]])
biases = np.array([0, 1, 2, 3])
weights2 = np.array([[1, 3], [0, 1], [2, 2], [3, 1]])
biases2 = np.array([2, 4])

start = DenseLayer('start', weights, biases)
process = Activation('process', 4, abs)
middle = DenseLayer('middle', weights2, biases2)
end = Activation('end', 2, math.sqrt)
full = MultiLayer('full', [start, process, middle, end])

print(start.get_config())
print(start.call(np.array([1, 3, 2])))
print()

print(process.get_config())
print(process.call(np.array([-1, 3, -5, 4])))
print()

print(end.get_config())
print(end.call(np.array([1, 3])))
print()

print(full.get_config())
print(full.call(np.array([-1, -3, 2])))
