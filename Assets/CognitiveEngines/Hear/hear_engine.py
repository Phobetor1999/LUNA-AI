import asyncio
import whisper
import os
from   pathlib import Path
# import webrtcvad

from Assets.Abstraction.Process.processBase import NeuralProcess
from Assets.Helpers.ConfigurationHelper.config_loader import loadConfiguration

class Hear_Engine(NeuralProcess):
    def __init__(self):
        super().__init__()
        script_dir = Path(__file__).parent.resolve()                 # Determina la directory corrente dello script
        config_path = script_dir / "config.yaml"                     # Percorso del file di configurazione

        if not config_path.exists(): raise FileNotFoundError(f"File di configurazione non trovato: {config_path}")

        # Carica la configurazione
        self.config                 = loadConfiguration(script_dir)  # Carica il file config.yaml dalla propria directory
        self.audio_settings         = self.config["audio_settings"]
        self.transcription_settings = self.config["transcription"]
        self.speaker_settings       = self.config["speaker_recognition"]
        self.model                  = None
        # self.vad                    = webrtcvad.Vad()
        #self.vad.set_mode(self.audio_settings["vad_mode"])

    async def initialize(self):
        """Inizializza il motore di Speech-to-Text."""

        print("Modello Whisper caricato correttamente!")
        print("Hear_Engine => SpeechToTextEngine: Caricamento modello Whisper...")
        self.model = whisper.load_model(self.transcription_settings["whisper_model"])
        print("Hear_Engine => SpeechToTextEngine: initialized.")

    def identify_speaker(self, audioStimulus):
        """ Metodo fittizio per identificare il parlante dall'audio.
            Deve essere implementato utilizzando un sistema di riconoscimento vocale."""
        
        # TODO: Logica per identificare lo speaker (placeholder)
        # Supponiamo che restituisca un ID speaker
        return "001"        
    
    async def handleStimulus(self, focusedSpeaker_id, audioStimulus):
        """Elabora audio simulando l'udito."""

        # Identifica il parlante attuale dall'audio
        identifiedSpeaker_id = self.identify_speaker(audioStimulus)

        # Verifica se l'audio proviene dal parlante su cui Luna è focalizzata
        if identifiedSpeaker_id != focusedSpeaker_id:
            print(f"Hear_Engine => Ignored: Audio is not from the focused speaker (expected: {focusedSpeaker_id}, got: {identifiedSpeaker_id}).")
            return None
        
        print(f"Hear_Engine => Recognized speaker '{focusedSpeaker_id}'. Proceeding with transcription...")
        print(f"Hear_Engine => SpeechToTextEngine: processing audio from speaker '{focusedSpeaker_id}' ")

        # Esegue la trascrizione dell'audio
        result = self.model.transcribe(audioStimulus)
        transcription = result["text"]
        print(f"Hear_Engine => Transcription result: {transcription}")
        return transcription
    