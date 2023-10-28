import requests
import yaml
from pathlib import Path

class Config:
    def __init__(self, config):
        self.base_url = config.get('api').get('base')
        self.endpoints = config.get('api').get('endpoints')
        self.bearer_token = config.get('api').get('bearer')


def extract(config, endpoint):
    headers = {
        'Authorization': 'Bearer ' + config.bearer_token,
        'X-Requested-With': 'XMLHttpRequest',
        'Role': 'Client',
        'Accept': 'application/json'
    }
    response = requests.get(f"{config.base_url}/{endpoint}", headers=headers)
    return response.text


def load_config():
    with open(Path(__file__).parent / 'config.yaml', 'r') as f:
        return yaml.safe_load(f)
    
def write_file(data, filename):
    print(f"Writing data to /data/{filename}.json")
    with open(Path(__file__).parent / 'data' / f"{filename}.json", 'w') as f:
        f.write(data)

print("Loading from config.yaml...")
config = Config(load_config())

endpoint_data = []
for endpoint in config.endpoints:
    print(f"Fetching data for endpoint {endpoint}")
    data = extract(config, endpoint)
    write_file(data, endpoint)
    endpoint_data.append(data)
    
print("Done, here's the data: \n")
print(endpoint_data)
