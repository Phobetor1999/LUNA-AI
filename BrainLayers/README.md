### I LAYERS DEL CERVELLO (BRAIN) di Luna-AI



# Punti Chiave

## Architettura Modulabile:
    Il sistema separa i principali layer cerebrali (cognitivo, emotivo etc), permettendo loro di funzionare in modo indipendente ma con la possibilità di comunicare.
    
    L'uso del metodo 'send_stimulus' consente un'eventuale estensione futura per inviare messaggi più complessi.

## Gestione Asincrona:
    La funzione asyncio.run garantisce l'esecuzione asincrona e coordinata dei layer.
    L'utilizzo di await asyncio.sleep(5) dà il tempo ai processi di gestire gli stimoli in modo simulato.
    Facilità di Estensione:

    I layer Cognitive_Layer, Emotional_Layer, Logical_Layer, Memory_Layer e Unconscious_Layer ereditano la propria struttura da NeuralProcess, facilitando l'integrazione di altri sistemi.

## Funzionamento
    Stimoli Diversificati:

    - Immagini (type: "image") → Inviate al VisionEngine.
    - Audio    (type: "audio") → Inviati al SpeechToTextEngine.
    - Testo    (type: "text")  → Inviato al TextToSpeechEngine.

## Parallelismo Naturale:
    I motori lavorano indipendentemente.
    Ogni motore è un'istanza di NeuralProcess e può elaborare stimoli asincroni.

## Facilità di Estensione:
    Nuovi motori possono essere aggiunti estendendo NeuralProcess integrandoli nei BrainLayers e in CognitiveEngines.