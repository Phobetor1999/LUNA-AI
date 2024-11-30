# Copyright 2022 S2DesignsTeam (㊙️anonimo㊙️).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import asyncio
import os
import json
import abc
from pathlib import Path
import yaml                          # Per gestire i file YAML
import logging                       # Utilizzato per il logging avanzato
from abc import ABC, abstractmethod
from multiprocess import Process 

class ANeuralProcess(ABC):
    
    #from Engines.libLogEngine import LogEngine

    """ 
    Classe astratta per definire la struttura base di un processo neurale. 
    """
    _name         : str       = "ANeuralProcessBase"      # Nome di base del Processo Neurale
    #_logEngine    : LogEngine = None
    _script_path  : str       = None                      # Percorso del file script 
    _am_i_active  : bool      = False                     # Flag che indica se il processo Neurale è attivo (True) o dormiente (False)
    _stimuli_queue = None  # Variabile per la coda degli stimoli

    #- [PROPERTIES]
    #--------------------------------------------------------------------------------------------------
    @property
    def am_i_active(self):
        """
        Verifica se il processo neurale è attivo.
        """
        return self._am_i_active
    
    @property
    def script_path(self): 
        """
        Percorso dello script.
        """
        return self._script_path
    
    @script_path.setter
    def script_path(self, value):
        if isinstance(value, Path):  # Controllo opzionale per assicurarsi che sia un oggetto Path
            self._script_path = value
        else:
            raise TypeError("script_path deve essere un oggetto Path.")


    #- [CONSTRUCTOR]
    #--------------------------------------------------------------------------------------------------
    def __init__(self):
        """
        Inizializza il Processo Neurale caricando automaticamente il file config.yaml 
        dal percorso dello script.
        """
        self._name       = "HearingEngine"
        if self.script_path is None:
            raise NotImplementedError(
                f"[{self.__class__.__name__}] La variabile 'script_path' deve essere definita nella classe concreta."
            )
        self.config                         = self._loadConfig()
        self._esternalStimuliDir            = os.path.join(self.script_path, "externalStimuli")
        self._incomingStimuliEvaluationTask = None
        self._stimuli_queue                 = asyncio.Queue()  # Coda per la comunicazione tra processi neurali
        
        # Configurazione del logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
      
    def _loadConfig(self):
        """ 
        Carica il file di configurazione 'config.yaml' presente nello stesso percorso della classe concreta.
        :return: Dizionario con la configurazione caricata. 
        """
        config_file = os.path.join(self.script_path, "config.yaml")

        if not os.path.exists(config_file):
            raise FileNotFoundError(f"File di configurazione non trovato: {config_file}")
        
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
        
    async def _readExternalStimuli(self):
        """
        Legge i file JSON dalla directory di input e restituisce una lista di stimoli.
        :return: Lista di dizionari rappresentanti gli stimoli.
        """
        if not self._esternalStimuliDir:
            raise ValueError(f"[{self.__class__.__name__}] Directory di input stimoli esterni non configurata.")
        
        stimuli = []
        for filename in os.listdir(self._esternalStimuliDir):
            file_path = os.path.join(self._esternalStimuliDir, filename)
            if filename.endswith('.json'):
                try:
                    with open(file_path, 'r') as f:
                        stimuli.append(json.load(f))
                except json.JSONDecodeError as e:
                    self.logger.error(f"[{self.__class__.__name__}] Errore nella decodifica di {filename}: {e}")

                except Exception as e:
                    print(f"[{self.__class__.__name__}] Errore durante la lettura di {filename}: {e}")
                finally:
                    try:
                        if os.Path.exists(file_path):
                            os.remove(file_path)  # Elimina il file dopo la lettura
                            self.logger.info(f"[{self.__class__.__name__}] File di stimolo esterno rimosso {file_path}: {e}")
                    except Exception as e:
                        self.logger.warning(f"[{self.__class__.__name__}] Impossibile eliminare il file di stimolo esterno {file_path}: {e}")
        return stimuli

    async def _evaluateIncomingStimuli(self):
        """
        Gestisce la comunicazione asincrona (ad esempio ricevere messaggi).
        """
        while self.am_i_active:
            try:            
                neuralStimuli = await self._stimuli_queue.get()
                externalStimuli = await self._readExternalStimuli()
                if neuralStimuli:
                    await self.handleSelfStimuli(neuralStimuli)
                if externalStimuli:
                    await self.handleExternalStimuli(externalStimuli)

            except asyncio.CancelledError:
                self.logger.info(f"[{self.__class__.__name__}] Valutazione stimoli interrotta.")
                break

            except Exception as e:
                self.logger.error(f"[{self.__class__.__name__}] Errore durante la valutazione degli stimoli: {e}")


    @abstractmethod
    async def initialize(self):
        """
        Metodo astratto per l'inizializzazione del Processo Neurale.
        Deve essere implementato dalle classi concrete.
        Da utilizzare per attribuire i valori di configurazione propri al Processo Neurale 
        che viene eseguito e ad istanziare componenti impiegati per il proprio funzionamento.
        """
        pass

    @abstractmethod
    async def handleSelfStimuli(self, message):
        """
        Gestisce lo Stimolo Neurale presente nella Message Queue degli stimoli interiori. 
        Al momento del richiamo di questo metodo il Processo Neurale 
        ancora non sa se è uno stimolo che deve tenere in considerazione ed elaborare.
        Qui dentro deve essere definita la logica check che serve al Processo Neurale per 
        capire se lo stimolo deve essere considerato e la propria logica di rielaborazione.
        Se è necessario da qui si può chiamare il metodo sendStimuli che invia un nuovo 
        stimolo con il risultato della rielaborazione del Processo Neurale effettuata sul 
        precedente stimolo.
        """
        pass

    @abstractmethod
    async def handleExternalStimuli(self, message):
        """
        Gestisce lo Stimolo Neurale presente nella Message Queue degli stimoli esterni. 
        Al momento del richiamo di questo metodo il Processo Neurale 
        ancora non sa se è uno stimolo che deve tenere in considerazione ed elaborare.
        Qui dentro deve essere definita la logica check che serve al Processo Neurale per 
        capire se lo stimolo deve essere considerato e la propria logica di rielaborazione.
        Qui si deve richiamare il metodo sendStimuli che invia lo stimolo esterno al message queue
        con per poter essere processato dal Processo Neurale di competenza.
        """
        pass    

    async def sendStimuli(self, stimuli):
        """
        Metodo per la comunicazione tra i vari processi neurali.
        :param stimuli: Dizionario con i dati elaborati.
        """
        try:
            await self._stimuli_queue.put(stimuli)
            self.logger.info(f"[{self.__class__.__name__}] Stimolo inviato: {stimuli}")
        except Exception as e:
            self.logger.error(f"[{self.__class__.__name__}] Errore durante l'invio dello stimolo: {e}")

    async def wakeUp(self):
        """
        Attiva il Processo Neurale e fa partire il thread della propria logica
        (definita nella classe concreta all'interno del metodo handleStimuli).
        """
        self.logger.info(f"[{self.__class__.__name__}] Avvio del Processo Neurale...")

        if self._am_i_active:
            raise RuntimeError("Il Processo Neurale è già attivo.")
         
        # Metodo astratto implementato dalla classe concreta
        await self.initialize()
        self._am_i_active = True

        # Avvia il task asincrono per gestire gli stimoli
        self._incomingStimuliEvaluationTask = asyncio.create_task(self._evaluateIncomingStimuli())

    async def sleep(self):
        """
        Mette il Processo Neurale a riposo (ferma la logica di processamento degli stimoli).
        """
        if not self.am_i_active:
            raise RuntimeError("Il Processo Neurale non è attivo.")        
        
        self._am_i_active = False
        if self._incomingStimuliEvaluationTask:
            # Annulla il task
            self._incomingStimuliEvaluationTask.cancel()
        try:
            await self._incomingStimuliEvaluationTask
        except asyncio.CancelledError:
            self.logger.info(f"[{self.__class__.__name__}] Processo messo a riposo.")
        except Exception as e:
            self.logger.error(f"[{self.__class__.__name__}] Errore durante il riposo del processo: {e}")  
        finally:
            self._incomingStimuliEvaluationTask = None