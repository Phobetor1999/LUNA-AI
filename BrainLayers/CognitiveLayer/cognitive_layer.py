from Assets.Abstraction.Process.processBase       import NeuralProcess
from Assets.CognitiveEngines.Vision.vision_engine import VisionEngine
from Assets.CognitiveEngines.Hear.hear_engine     import Hear_Engine
from Assets.CognitiveEngines.Speech.speech_engine import Speech_Engine

class CognitiveLayer(NeuralProcess):
    def __init__(self):
        super().__init__()
        self.vision_engine = VisionEngine()
        self.stt_engine    = Hear_Engine()
        self.tts_engine    = Speech_Engine()

    async def initialize(self):
        """Inizializza tutti i motori del layer cognitivo."""
        await self.vision_engine.wakeUp()
        await self.stt_engine.wakeUp()
        await self.tts_engine.wakeUp()
        print("CognitiveLayer: all engines initialized.")

    async def handle_stimulus(self, message):
        """Distribuisce il messaggio al motore appropriato."""
        if message["type"] == "image":
            return await self.vision_engine.send_stimulus(message["data"])
        elif message["type"] == "audio":
            return await self.stt_engine.send_stimulus(message["data"])
        elif message["type"] == "text":
            return await self.tts_engine.send_stimulus(message["data"])
        else:
            print(f"CognitiveLayer: Unknown stimulus type {message}")

    async def sleep(self):
        """Mette a riposo tutti i motori."""
        await self.vision_engine.sleep()
        await self.stt_engine.sleep()
        await self.tts_engine.sleep()
        print("CognitiveLayer: all engines stopped.")