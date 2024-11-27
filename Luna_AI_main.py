import asyncio
from Assets.CognitiveEngines.Hear.hear_engine import Hear_Engine
from BrainLayers.CognitiveLayer.cognitive_layer import CognitiveLayer
from BrainLayers.EmotionalLayer.emotional_layer import Emotional_Layer

import whisper

model = whisper.load_model("base")
print("Modello Whisper caricato correttamente!")

async def main():
    hearSense = Hear_Engine()
    # Crea i vari processi neurali (layer del cervello)
    #cognitive_layer = CognitiveLayer("Sistema cognitivo")
    #emotive_layer   = Emotional_Layer("Sistema emotivo - empatico")

    # Risveglia i processi neurali
    hearSense.wakeUp()
    #await cognitive_layer.wakeUp()
    #await emotive_layer.wakeUp()
    
    # Comunica tra i processi neurali
    #await cognitive_layer.send_stimulus("Messaggio dalla Corteccia cerebrale")
    #await emotive_layer.send_stimulus("Messaggio dal Sistema limbico")

    # Attendere che i processi lavorino per un po'
    #await asyncio.sleep(5)

    # Mette a riposo i processi neurali
    hearSense.sleep()
    #await cognitive_layer.sleep()
    #await emotive_layer.sleep()

    print("Tutti i processi neurali sono stati messi a riposo.")

# Avvia la funzione main
asyncio.run(main())