#  Setup del progetto: Verifica e configurazione dell'ambiente di sviluppo (Python, dipendenze, ecc.).
<UL> 

## 1. Verifica dell'ambiente di sviluppo:

<UL> 
<LI>

### 1.1 Verifica di Python

Controllare che Python (min. 3.10) sia installato correttamente.
<UL> 
<LI>

#### [Step 1] Apri un terminale e controlla la versione di Python installata:
```console
python --version
```
Risultato atteso

<UL> 
    <li>[SUCCESSO] Se la versione è >= 3.10.</li>
    <li>[FALLIMENTO] Se la versione è < 3.10.</li>
</UL>
[SU FALLIMENTO]: scarica e installa la versione più recente da www.python.org/downloads/
</LI>

<LI>

#### [Step 2] Aggiornare o installare pip
Assicurati che pip sia aggiornato:
```console
python -m pip install --upgrade pip
```
</LI>
</UL> 
</LI>

<LI>

### 1.2 Installazione e configurazione di virtualenv
<UL> 
<LI>

#### [Step 1.2.1] Installa virtualenv se non è già presente:
```console
python -m pip install virtualenv
```
</LI>
<LI>

#### [Step 1.2.2] Crea un ambiente virtuale nella directory del progetto:
```console
python -m virtualenv luna_env
```
</LI>
<LI>

#### [Step 1.2.3] Attiva l'ambiente virtuale:
- Windows:
```console
.\luna_env\Scripts\activate
```
- Linux:
```console
source luna_env/bin/activate
```
</LI>
</UL> 
</LI>

<LI>

### 1.3 Verifica dei driver NVIDIA, CUDA e cuDNN
<UL> 
<LI>

#### [Step 1.3.1] Verifica se la tua GPU è riconosciuta:
  ```console 
  nvidia-smi
  ```
Risultato atteso:
<UL> 
    <LI>[SUCCESSO] L'output mostra le caratteristiche della GPU nvidia.</LI>
    <LI>[FALLIMENTO] L'output NON mostra le caratteristiche della GPU nvidia.</LI>
</UL>
[SU FALLIMENTO]: Se la GPU non è riconosciuta, installa i driver dal sito ufficiale NVIDIA.
</LI>
<LI>

  #### [Step 1.3.2] Controlla la versione di CUDA installata:
  ```console
  nvcc --version
  ```
  Risultato atteso:
  <UL> 
    <LI>[SUCCESSO] L'output mostra il seguente messaggio (o simili):

```console    
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2024 NVIDIA Corporation
Built on Wed_Oct_30_01:18:48_Pacific_Daylight_Time_2024
Cuda compilation tools, release 12.6, V12.6.85
Build cuda_12.6.r12.6/compiler.35059454_0
```

  </LI>
  <LI>[FALLIMENTO] L'output mostra il seguente messaggio:

  ```console
  nvcc : Termine 'nvcc' non riconosciuto come nome di cmdlet, funzione, programma eseguibile o file script. Controllare
  l'ortografia del nome o verificare che il percorso sia incluso e corretto, quindi riprovare.                         
  In riga:1 car:1                                                                                                      
  + nvcc --version                                                                                                     
  + ~~~~                                                                                                               
              + CategoryInfo          : ObjectNotFound: (nvcc:String) [], CommandNotFoundException                             
              + FullyQualifiedErrorId : CommandNotFoundException}$$
  ```
  </LI>
  </UL>
  [SU FALLIMENTO] L'errore che hai ricevuto indica che il comando nvcc non è riconosciuto, probabilmente perché:
  <UL> 
    <LI>CUDA non è installato sul tuo sistema.</LI>
    <LI>CUDA è installato ma non è nel PATH di sistema, quindi il terminale non riesce a trovare il comando nvcc.</LI>
  </UL>

  [SOLUZIONE] Passaggi per risolvere il problema:
  <UL> 
  <LI> 
  
  #### [Step 1.3.2.1] Verifica se CUDA è installato
  Controlla la presenza della directory CUDA nel tuo sistema:
  <UL> 
    <LI> Windows: </LI>
  Cerca la cartella C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA. La versione di CUDA è solitamente indicata nel nome della sottocartella, ad esempio v12.0.
    <LI> Linux: </LI>
  Controlla se esiste una directory come /usr/local/cuda.
  </UL> 
  </LI>

  <LI>
  
  #### [Step 1.3.2.2] Installa CUDA se necessario
  Se non trovi CUDA sul tuo sistema:
  <UL> 
    <LI>Scarica l'installer di CUDA compatibile con la tua GPU e sistema operativo dal sito ufficiale NVIDIA CUDA Toolkit https://developer.nvidia.com/cuda-toolkit .</LI>
    Durante l'installazione, assicurati di spuntare l'opzione per aggiungere i binari di CUDA al PATH.
  </UL>
  </LI>

  <LI>

  #### [Step 1.3.2.3] Aggiungi CUDA al PATH (se già installato)
  Se CUDA è installato ma il comando nvcc non funziona, è probabile che i percorsi binari non siano configurati correttamente nel tuo sistema.
  <UL> 
  Aggiungere CUDA al PATH su Windows:
    <LI>Apri Pannello di Controllo > Sistema > Impostazioni Avanzate del Sistema > Variabili d'Ambiente.</LI>
    <LI>Nella sezione Variabili di Sistema, trova la variabile Path e seleziona Modifica.</LI>
    <LI>Aggiungi i seguenti percorsi (adatta i numeri di versione se necessario):</LI>

```console
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\bin
```
```console
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.0\libnvvp
```
  </UL>
  <BR>
  <UL> 
  Aggiungere CUDA al PATH su Linux:
  <LI>Apri il terminale e modifica il file .bashrc (o .zshrc se usi Zsh):

```console
nano ~/.bashrc
```
  </LI>
  <LI>Aggiungi le seguenti righe alla fine del file (adatta il percorso alla tua versione di CUDA):

```console
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
```
  <LI>Salva le modifiche e aggiorna la configurazione:

```console
source ~/.bashrc
```
  </LI>
  </LI>
  </UL> 
  <LI>

  #### [Step 1.3.2.4] Salva e chiudi tutto.
  Riavvia il terminale e verifica di nuovo con:

```console
nvcc --version
```
  </LI>

  * La versione deve essere compatibile con PyTorch o TensorFlow che useremo.
</LI>
</UL> 

<LI>

  #### [Step 1.3.3] Installa/cuDNN:
      - Scarica e installa la versione di cuDNN corrispondente alla tua versione di CUDA dal sito NVIDIA (https://developer.nvidia.com/cudnn)
</LI>
<LI>

  #### [Step 1.3.4] Configura CUDA/cuDNN:
      - Aggiungi i percorsi binari di CUDA/cuDNN al tuo PATH (se non lo hai già fatto).
</LI>
</UL> 


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
</UL> 