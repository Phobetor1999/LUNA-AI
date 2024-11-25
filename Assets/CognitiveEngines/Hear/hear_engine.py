import asyncio
import whisper
import webrtcvad

from Assets.Abstraction.Process.processBase import NeuralProcess
from Assets.Helpers.ConfigurationHelper.config_loader import loadConfiguration



class Hear_Engine(NeuralProcess):
    def __init__(self, config_dir):
        super().__init__()
        self.config                 = loadConfiguration(config_dir)  # Carica il file config.yaml dalla propria directory
        self.audio_settings         = self.config["audio_settings"]
        self.transcription_settings = self.config["transcription"]
        self.speaker_settings       = self.config["speaker_recognition"]
        self.model                  = None
        self.vad                    = webrtcvad.Vad()
        self.vad.set_mode(self.audio_settings["vad_mode"])

    async def initialize(self):
        """Inizializza il motore di Speech-to-Text."""
        print("Hear_Engine => SpeechToTextEngine: Caricamento modello Whisper...")
        self.model = whisper.load_model(self.transcription_settings["whisper_model"])
        print("Hear_Engine => SpeechToTextEngine: initialized.")

    async def handle_stimulus(self, message):
        """Elabora audio simulando l'udito."""
        print(f"Hear_Engine => SpeechToTextEngine: processing audio - {message}")
        # Simula la trascrizione audio
        result = f"Transcribed audio: {message}"
        print(f"Hear_Engine => SpeechToTextEngine result: {result}")
        return result
    