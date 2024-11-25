import asyncio
from abc import ABC, abstractmethod

class NeuralProcess(ABC):
    def __init__(self):
        self._am_i_active                       = False
        self._incoming_stimulus_evaluation_task = None
        self._stimulus_queue                    = asyncio.Queue()  # Coda per la comunicazione tra processi neurali
      
    @abstractmethod
    async def initialize(self):
        """Metodo che inizializza l'attività del processo (cervello)."""
        pass

    @abstractmethod
    async def handle_stimulus(self, message):
        """Gestisce il messaggio ricevuto dal processo."""
        pass

    async def send_stimulus(self, message):
        """Metodo per la comunicazione tra i vari processi neurali."""
        await self._stimulus_queue.put(message)

    async def wakeUp(self):
        """Risveglio del processo neurale (avvia il processo)."""

        if self._am_i_active:
            raise RuntimeError("Il processo è già attivo.")

        await self.initialize()
        self._am_i_active = True
        self._incoming_stimulus_evaluation_task = asyncio.create_task(self._incoming_stimulus_evaluation())

    async def sleep(self):
        """Mette il processo neurale a riposo (ferma il processo)."""

        if not self._am_i_active:
            raise RuntimeError("Il processo non è attivo.")        
        
        self._am_i_active = False
        if self._incoming_stimulus_evaluation_task:
            self._stimulus_queue.put_nowait(None)  # Segnale di stop
            await self._incoming_stimulus_evaluation_task
            self._incoming_stimulus_evaluation_task = None

    async def _incoming_stimulus_evaluation(self):
        """Gestisce la comunicazione asincrona (ad esempio ricevere messaggi)."""
        while self._am_i_active:
            message = await self._stimulus_queue.get()
            await self.handle_stimulus(message)

    @property
    def am_i_active(self):
        """Verifica se il processo neurale è attivo."""
        return self._am_i_active