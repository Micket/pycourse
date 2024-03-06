# Idea here is to borrow from what TF/Keras/PyTorch does and implement "Layer" classes for machine learning.

class Layer(ABC):
    def __init__(self, name, input_size, output_size):
        self.name = name
        self.input_size = input_size
        self.output_size = input_size

    @abstractmethod
    def call(self, inputs):
        pass

    def get_config(self):
        return {'name': self.name, 
                'input_size': self.input_size, 
                'output_size': self.output_size}


class Identity(Layer):  # this does nothing
    def build(self, input_shape):
        pass

    def call(self, inputs):
        return inputs

    def get_config(self):
        d = super().get_config()
        d['type'] = 'Identity'
        return d


class Activation(Layer):
    def __init__(self, name, shape, fun):
        super().__init__(name, shape, shape)
        self.fun = fun

    def call(self, inputs):
        if self.input_size != len(inputs):
            return IndexError("Input size mismatch")
        return [self.fun(i) i in inputs]

    def get_config(self):
        d = super().get_config()
        d['type'] = 'Activation'
        d['fun'] = str(fun)
        return d


class DenseLayer(Layer):
    def __init__(self, name, input_size, output_size):
        super().__init__(name, input_size, output_size)
        self.weights = np.random.rand(input_size, output_size)
        self.biases = [0]*output_size

    def call(self, inputs):
        return np.dot(self.weights, inputs) + self.biases

    def get_config(self):
        d = super().get_config()
        d['type'] = 'DenseLayer'
        d['weights'] = self.weights
        d['weights'] = self.biases
        return d


class MultiLayer(Layer):
    def __init__(self, self.layers):
        self.layers = layers

    def call(self, inputs):
        x = inputs
        for layer in self.layers:
            x = layer.call(x)
        return x

    def get_config(self):
        d = super().get_config()
        d['type'] = 'DenseLayer'
        d['layers'] = [layer.get_config() for layer in self.layers]


