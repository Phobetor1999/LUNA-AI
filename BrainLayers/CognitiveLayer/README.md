### STRATO COGNITIVO di Luna-AI (CognitiveLayer)

## Descrizione
Il Layer Cognitivo è responsabile per la simulazione delle funzioni Cognitive del sistema. Questo layer gestisce l'elaborazione di informazioni che non sono immediatamente accessibili alla consapevolezza cosciente, ma che influiscono sul comportamento e sulle decisioni del sistema.

## Funzionalità
- Simulazione di processi inconsci che influenzano le decisioni logiche ed emotive.
- Gestione dei dati non verbali o semi-verbali che emergono da altre interazioni nel sistema.
- Interazione con altri layer (come il layer emotivo e cognitivo) per influenzare la risposta finale.

## Interazioni
- Il layer inconscio interagisce direttamente con il **Layer Emotivo** per gestire stati inconsci di emozioni.
- Comunica con il **Layer Cognitivo** per influenzare la razionalità delle risposte.

## Metodo di Inizializzazione
- Il Layer Inconscio viene inizializzato tramite il metodo `Init` del processo dell'engine.
- L'attivazione del layer avviene tramite il metodo `Activate` che prepara il sistema a raccogliere ed elaborare i segnali inconsci.

## Esempio di utilizzo
```python
from layers.unconscious_layer.unconscious_layer import UnconsciousLayer

# Creazione del layer inconscio
unconscious_layer = UnconsciousLayer()

# Inizializzazione del layer
unconscious_layer.Init()

# Attivazione del layer
unconscious_layer.Activate()

# Messa in pausa del layer
unconscious_layer.Sleep()