# Get the entitites with context information at the Orion Context Broker

import requests
from integration_modules.setup_address import set_address

address = set_address()


def get_entities_by_type():
    url = 'http://'+address+':1026/v2/types?options=values'
    response = requests.get(url)

    if (response.status_code == 200):
        return response.json()
    else:
        return 'Query failed'
