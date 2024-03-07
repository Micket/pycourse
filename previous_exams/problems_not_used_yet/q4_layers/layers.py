# Idea here is to borrow from what TF/Keras/PyTorch does and implement "Layer" classes for machine learning.
import abc


class Layer(abc.ABC):
    def __init__(self, name, input_size, output_size):
        self.name = name
        self.input_size = input_size
        self.output_size = output_size

    @abc.abstractmethod
    def call(self, inputs):
        pass

    def get_config(self):
        return {'name': self.name, 
                'input_size': self.input_size, 
                'output_size': self.output_size}


class DenseLayer(Layer):
    def __init__(self, name, weights, biases):

        if weights.shape[1] != len(biases):
            raise ValueError("Size if weights and biases does not match!")

        super().__init__(name, weights.shape[0], weights.shape[1])
        self.weights = weights
        self.biases = biases

    def call(self, inputs):
        return inputs.dot(self.weights) + self.biases

    def get_config(self):
        d = super().get_config()
        d['type'] = 'DenseLayer'
        d['weights'] = self.weights
        d['biases'] = self.biases
        return d


class Activation(Layer):
    def __init__(self, name, size, fun):
        super().__init__(name, size, size)
        self.fun = fun

    def call(self, inputs):
        if self.input_size != len(inputs):
            raise IndexError("Input size mismatch")
        return np.array([self.fun(i) for i in inputs])

    def get_config(self):
        d = super().get_config()
        d['type'] = 'Activation'
        d['fun'] = str(self.fun)
        return d


class MultiLayer(Layer):
    def __init__(self, name, layers):
        super().__init__(name, layers[0].input_size, layers[-1].output_size)
        self.layers = layers

    def call(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer.call(x)
        return x

    def get_config(self):
        d = super().get_config()
        d['type'] = 'MultiLayer'
        d['layers'] = [layer.get_config() for layer in self.layers]
        return d


# Testing code:
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
