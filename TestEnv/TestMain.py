import sys
import os
from pathlib import Path

# Percorso base del progetto
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Import della classe NeuralProcess
from Assets.Abstraction.Process import NeuralProcess

# Aggiungi il percorso principale del progetto al sys.path
sys.path.append(str(BASE_DIR))

from Assets.CognitiveEngines.Hear import Hear_Engine

# Dummy per simulare il focus
def focus_dummy(speaker_id): return '001'

# Callback per elaborare il testo trascritto
def semantic_callback(speaker_id, transcription):
    print(f"[Profilo: {speaker_id}] -> {transcription}")

# Inizializza il motore
engine = Hear_Engine()

# Elabora un file audio di test
engine.handleStimulus("001", "TestData/Sounds/Speakers_samples/Speaker_001_sample_001.wav")