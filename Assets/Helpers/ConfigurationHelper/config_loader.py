import yaml
import os

def loadConfiguration(config_dir):
    """
    Carica un file `config.yaml` dalla directory specificata.
    
    :param config_dir: Directory contenente il file `config.yaml`.
    :return: Dizionario con i parametri di configurazione.
    """
    config_path = os.path.join(config_dir, "config.yaml")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configurazione non trovata: {config_path}")
    
    with open(config_path, "r") as file:
        return yaml.safe_load(file)