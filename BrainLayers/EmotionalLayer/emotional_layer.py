import asyncio
from Assets.Abstraction.Process.processBase import NeuralProcess

# Classe derivata che simula il layer del processo Emozionale/Emptatico del cervello
class EmotionalLayer(NeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name