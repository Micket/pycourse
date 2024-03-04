# Idea here is to borrow from what TF/Keras/PyTorch does and implement "Layer" classes for machine learning.


class Layer(ABC):
    @abstractmethod
    def build(self, input_shape):
        pass

    @abstractmethod
    def call(self, inputs):
        pass

    @abstractmethod
    def get_config(self):
        pass

class Identity(Layer):
    pass

class Activation(Layer):
    pass

class DenseLayer(Layer):
    pass

class Masking(Layer):
    pass
