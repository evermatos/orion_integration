# Performs query requests to the Orion Context Broker

import requests
from integration_modules.setup_address import set_address

address = set_address()


def get_entities():
    url = 'http://'+address+':1026/v2/entities?options=keyValues'
    response = requests.get(url)

    if (response.status_code == 200):
        return response.json()
    else:
        return 'Query failed'


def get_entities_filter(list_of_filters):
    url = 'http://'+address+':1026/v2/entities?options=keyValues'

    for x in list_of_filters:
        url_aux = '&' + x[0] + x[1]
        url = url + url_aux

    response = requests.get(url)

    if (response.status_code == 200):
        return response.json()
    else:
        return 'Query failed'
