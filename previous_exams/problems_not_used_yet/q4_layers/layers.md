---
header-includes:
        - \usepackage[a4paper,left=1.9cm, right=1.9cm, top=1.5cm, bottom=1.9cm]{geometry}
---

# Question 4 (6p)

In the popular field of machine learning the typical approach is to use multiple layers of different types to process input vectors.
Each layer takes a fixed sized vector as input, and produces a fixed sized vector as output (possibly of different size than the input).

## Part A: Layer base class (1p)

Create an abstract base class **Layer** which:

- stores the `name`, `input_size`, `output_size` (which all layers must have)
- has the abstract method `call` which takes an `input_vector` for processing
- has the method `get_config` which returns a dictionary with the name and input and output sizes (see examples) which can be used for saving a model to disk

## Part B: DenseLayer (1.5p)

Create a subclass of **Layer**, **DenseLayer** which takes a set of `weights` and `biases` (`NumPy` arrays) as input.
Here `weights` is a 2D array where the rows match the input size, and the columns match the output size. `biases` is 1D array which has the same size as the output.

- The constructor takes `weights` and `biases` and should verify that the sizes of them are compatible, if not raise an appropriate exception with a helpful message.
- `call` computes $x \cdot w + b$ where $x$ is the input vector, $w$ are the weights and $b$ are the biases.
- `get_config` should be overloaded to add `type` set to `'DenseLayer'` as well as the additional `weights` and `biases`.

## Part C: Activation (1.5p)

Create a subclass of **Layer**, **Activation** which applies a given function to all elements of the vector.

- The constructor takes a `size` (output size equals input size) and function pointer `fun`. 
- `call`  computes $f(x_i)$ for each element $x_i$ in the input vector. Verify that the input sizes is correct, otherwise throw an appropriate exception with a helpful message.
- `get_config` overloaded to add `type` set to `Activation` as well as the additional `fun`.

## Part D: MultiLayer (2p)

Create a subclass of **Layer**, **MultiLayer** which applies several layers in sequence, passing the output from one as input to the next.

- The constructor takes a list of layers.
- `call` passes the input to the first layer, passing the output of each layer to the next, returning the final output.
- `get_config` overloaded to add `type` set to `'MultiLayer'` as well as the additional `layers` which contain a list of the config for each layer.

\newpage
**Example**:

```python
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
```

**Output**:
```python
{'name': 'start', 'input_size': 3, 'output_size': 4, 'type': 'DenseLayer', 
    'weights': array([[1, 2, 0, 1], [3, 1, 1, 0], [4, 2, 1, 1]]), 'biases': array([0, 1, 2, 3])}
[18 10  7  6]

{'name': 'process', 'input_size': 4, 'output_size': 4, 'type': 'Activation', 
    'fun': '<built-in function abs>'}
[1 3 5 4]

{'name': 'end', 'input_size': 2, 'output_size': 2, 'type': 'Activation', 
    'fun': '<built-in function sqrt>'}
[1.         1.7320508075688772]

{'name': 'full', 'input_size': 3, 'output_size': 2, 'type': 'MultiLayer', 'layers': [
  {'name': 'start', 'input_size': 3, 'output_size': 4, 'type': 'DenseLayer', 
    'weights': array([[1, 2, 0, 1], [3, 1, 1, 0], [4, 2, 1, 1]]), 'biases': array([0, 1, 2, 3])},
  {'name': 'process', 'input_size': 4, 'output_size': 4, 'type': 'Activation', 
    'fun': '<built-in function abs>'},
  {'name': 'middle', 'input_size': 4, 'output_size': 2, 'type': 'DenseLayer', 
    'weights': array([[1, 3], [0, 1], [2, 2], [3, 1]]), 'biases': array([2, 4])},
  {'name': 'end', 'input_size': 2, 'output_size': 2, 'type': 'Activation', 
    'fun': '<built-in function sqrt>'}]}
[4.242640687119285 4.    ]
```


