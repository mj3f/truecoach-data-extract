# import requests
import yaml
from pathlib import Path

def load_config():
    with open(Path(__file__).parent / 'config.yaml', 'r') as f:
        return yaml.safe_load(f)
    
config = load_config()
print(config)




