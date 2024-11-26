import asyncio
from Assets.Abstraction.Process.processBase import NeuralProcess

# Classe derivata che simula il layer pel processo Inconscio del cervello
class UnconsciousLayer(NeuralProcess):
    def __init__(self, layer_name):
        super().__init__()
        self.layer_name = layer_name