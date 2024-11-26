#  TO DO:

 - [task] Setup del progetto: Verifica e configurazione dell'ambiente di sviluppo (Python, dipendenze, ecc.). 
   [task descr] 
    1. Verifica dell'ambiente di sviluppo:
        - Controllare che Python (min. 3.10) sia installato correttamente.
        - Aggiornare o installare pip, virtualenv e i driver per la GPU NVIDIA.
        - Verificare che CUDA e cuDNN siano configurati per PyTorch/TensorFlow.
    2. Configurazione delle dipendenze:
        - Creare un file requirements.txt con le librerie necessarie:
            a) torch, transformers, datasets (per LLM).
            b) whisper (per Speech-to-Text).
            c) pyttsx3 o TTS (per Text-to-Speech).
        - Impostare un ambiente virtuale con tutti i pacchetti installati.

 - [task] Definizione del primo engine o layer: Sviluppo di un componente iniziale, come il modulo LLM o un layer di base (es. UnconsciousLayer).
   [task descr]
    1. Sviluppo del modulo base (es. UnconsciousLayer):
        - Creare una struttura dati per memorizzare e gestire "informazioni inconsce".
        - Implementare algoritmi per aggiornamenti passivi, come una coda FIFO per concetti meno rilevanti.
    2. Modello LLM:
        - Decidere se utilizzare un LLM preaddestrato o addestrarne uno da zero.
        - Sviluppare una pipeline per gestire input/output del modello.

 - [task] Testing e validazione: Creazione di test automatizzati per i moduli già presenti o in via di sviluppo.
   [task descr]
    1. Scrivere test automatizzati per le funzionalità dei moduli:
        - Test unitari per verificare la corretta gestione della memoria nel layer.
        - Test funzionali per garantire che i moduli comunichino correttamente.
    2. Sviluppare un set di input di prova per verificare la coerenza dell'elaborazione del linguaggio.
 
 - [task] Integrazione: Progettazione della comunicazione tra gli engine e i brain layers.
   [task descr]
    1. Progettare API interne tra i layer del sistema.
    2. Decidere un protocollo di comunicazione (es. gRPC, messaggistica asincrona, funzioni dirette).
 
 - [task] Focus su una funzionalità chiave: Ad esempio, l'elaborazione del linguaggio naturale, l'empatia, o il ragionamento logico.
   [task descr]
    -   Implementare e migliorare una capacità distintiva, come l'elaborazione di sentimenti nel linguaggio.


 # DONE:
