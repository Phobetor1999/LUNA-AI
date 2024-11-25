import asyncio
from Assets.Abstraction.Process.processBase import NeuralProcess

# Un esempio di classe derivata che simula un layer del cervello
class EmotionalLayer(NeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name