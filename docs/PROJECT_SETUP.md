#  Setup del progetto: Verifica e configurazione dell'ambiente di sviluppo (Python, dipendenze, ecc.).

##   1. Verifica dell'ambiente di sviluppo:

###      1.1 Verifica di Python
Controllare che Python (min. 3.10) sia installato correttamente.
Steps: 

  1.1.a Apri un terminale e controlla la versione di Python installata:
  ```console
  python --version
  ```

  Risultato atteso:
  - [SUCCESSO] Se la versione è >= 3.10.
  - [FALLIMENTO] Se la versione è < 3.10.
  
  SU FALLIMENTO: scarica e installa la versione più recente da www.python.org/downloads/.

  1.1.b) Aggiornare o installare pip
  Assicurati che pip sia aggiornato:
  ```console
  python -m pip install --upgrade pip
  ```
                
###      1.2 Installazione e configurazione di virtualenv
Steps:

  1.2.a) Installa virtualenv se non è già presente:
  ```console
  python -m pip install virtualenv
  ```

  1.2.b) Crea un ambiente virtuale nella directory del progetto:
  ```console
  python -m virtualenv venv
  ```

  1.2.c) Attiva l'ambiente virtuale:
  - Windows:
  ```console
  .\venv\Scripts\activate
  ```

  - Linux:
  ```console
  source venv/bin/activate
  ```

###      1.3 Verifica dei driver NVIDIA, CUDA e cuDNN
Steps:

  1.3.a) Verifica se la tua GPU è riconosciuta:
  ```console
  nvidia-smi
  ```

  Risultato atteso:
  
  - [SUCCESSO] L'output mostra le caratteristiche della GPU nvidia.
  - [FALLIMENTO] L'output NON mostra le caratteristiche della GPU nvidia.
                  
  SU FALLIMENTO: Se la GPU non è riconosciuta, installa i driver dal sito ufficiale NVIDIA.

  1.3.b) Controlla la versione di CUDA installata:
  ```console
  nvcc --version
  ```

  Risultato atteso:

  - [SUCCESSO] L'output mostra il seguente messaggio:                
  - [FALLIMENTO] L'output mostra il seguente messaggio:
  ```console
  nvcc : Termine 'nvcc' non riconosciuto come nome di cmdlet, funzione, programma eseguibile o file script. Controllare
  l'ortografia del nome o verificare che il percorso sia incluso e corretto, quindi riprovare.                         
  In riga:1 car:1                                                                                                      
  + nvcc --version                                                                                                     
  + ~~~~                                                                                                               
              + CategoryInfo          : ObjectNotFound: (nvcc:String) [], CommandNotFoundException                             
              + FullyQualifiedErrorId : CommandNotFoundException}$$
  ```
  * La versione dovrebbe essere compatibile con PyTorch o TensorFlow che useremo.

  1.3.c) Installa/cuDNN:
      - Scarica e installa la versione di cuDNN corrispondente alla tua versione di CUDA dal sito NVIDIA (https://developer.nvidia.com/cudnn)

  1.3.d) Configura CUDA/cuDNN:
      - Aggiungi i percorsi binari di CUDA/cuDNN al tuo PATH (se non lo hai già fatto).

#   2.: Configurazione delle dipendenze

##      2.1 Creazione del file requirements.txt
  Crea un file requirements.txt nella directory del progetto con il seguente contenuto:
  ```console
  torch
  transformers
  datasets
  whisper
  pyttsx3
  ```
  Se preferisci un framework avanzato per TTS, sostituisci pyttsx3 con 'TTS' (https://github.com/coqui-ai/TTS):

##      2.2 Installazione delle dipendenze
  Dopo aver attivato l'ambiente virtuale (VEDI PUNTO 1.2.c), esegui:
  ```console
  pip install -r requirements.txt
  ```
