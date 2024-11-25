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

#  Setup del progetto: Verifica e configurazione dell'ambiente di sviluppo (Python, dipendenze, ecc.).

#   1. Verifica dell'ambiente di sviluppo:

##      1.1 Verifica di Python
            Controllare che Python (min. 3.10) sia installato correttamente.
            Steps: 
            a) Apri un terminale e controlla la versione di Python installata:
                <CODE>python --version</CODE>

                Risultato atteso:
                Se la versione è >= 3.10. ==> [SUCCESSO]
                Se la versione è < 3.10.  ==> [FALLIMENTO]
                [FALLIMENTO]: scarica e installa la versione più recente da python.org.

            b) Aggiornare o installare pip
                Assicurati che pip sia aggiornato:
                <CODE>python -m pip install --upgrade pip</CODE>
                
##      1.2 Installazione e configurazione di virtualenv
            Steps:
            a) Installa virtualenv se non è già presente:
                <CODE>python -m pip install virtualenv</CODE>

            b) Crea un ambiente virtuale nella directory del progetto:
                <CODE>python -m virtualenv venv</CODE>

            c) Attiva l'ambiente virtuale:
                - Windows:
                <CODE>
                    .\venv\Scripts\activate
                </CODE>

                - Linux:
                <CODE>
                    source venv/bin/activate
                </CODE>

##      1.3 Verifica dei driver NVIDIA, CUDA e cuDNN
            Steps:
            a) Verifica se la tua GPU è riconosciuta:
                <CODE>
                    nvidia-smi
                </CODE>

                Risultato atteso:
                - l'output mostra le caratteristiche della GPU nvidia     ==> [SUCCESSO]
                - l'output NON mostra le caratteristiche della GPU nvidia ==> [FALLIMENTO]
                
                [FALLIMENTO]: Se la GPU non è riconosciuta, installa i driver dal sito ufficiale NVIDIA.

            b) Controlla la versione di CUDA installata:
                <CODE>
                    nvcc --version
                </CODE>

                Risultato atteso:

                - l'output mostra il seguente messaggio:
                ==>[SUCCESSO]
                
                - l'output mostra il seguente messaggio:
                <PRE>
                    nvcc : Termine 'nvcc' non riconosciuto come nome di cmdlet, funzione, programma eseguibile o file script. Controllare
                    l'ortografia del nome o verificare che il percorso sia incluso e corretto, quindi riprovare.                         
                    In riga:1 car:1                                                                                                      
                    + nvcc --version                                                                                                     
                    + ~~~~                                                                                                               
                        + CategoryInfo          : ObjectNotFound: (nvcc:String) [], CommandNotFoundException                             
                        + FullyQualifiedErrorId : CommandNotFoundException                                                               
                </PRE>
                ==> [FALLIMENTO]
                
                * La versione dovrebbe essere compatibile con PyTorch o TensorFlow che useremo.

            c) Installa/cuDNN:
                - Scarica e installa la versione di cuDNN corrispondente alla tua versione di CUDA dal sito NVIDIA (https://developer.nvidia.com/cudnn)

            d) Configura CUDA/cuDNN:
                - Aggiungi i percorsi binari di CUDA/cuDNN al tuo PATH (se non lo hai già fatto).

#   2.: Configurazione delle dipendenze

##      2.1 Creazione del file requirements.txt
            Crea un file requirements.txt nella directory del progetto con il seguente contenuto:
            <CODE>
                torch
                transformers
                datasets
                whisper
                pyttsx3
            </CODE>
            Se preferisci un framework avanzato per TTS, sostituisci pyttsx3 con 'TTS' (https://github.com/coqui-ai/TTS):

##      2.2 Installazione delle dipendenze
            Dopo aver attivato l'ambiente virtuale (VEDI PUNTO 1.2.C), esegui:
            <CODE>
                pip install -r requirements.txt
            </CODE>


# Passi successivi
    Verifica che tutto sia configurato correttamente.