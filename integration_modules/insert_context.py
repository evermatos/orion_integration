# Add information to the Orion Context Broker

import requests
from integration_modules.setup_address import set_address

address = set_address()


def test_orion():
    url = 'http://'+address+':1026/version'
    response = requests.get(url)

    if (response.status_code == 200):
        return 'Response: {}'.format(response.json()["orion"])
    else:
        return 'Connection failed'


def put_entity(entity):
    url = 'http://'+address+':1026/v2/entities/'
    response = requests.post(url, json=entity)
    if (response.status_code == 201):
        return 'Entity inserted'
    else:
        return 'Action failed'


def update_specific_atribute(entity_id, entity_atribute, entity_context):
    url = 'http://'+address+':1026/v2/entities/' + entity_id + \
        '/attrs/' + entity_atribute + '/value'
    print(url)
    response = requests.put(url,
                            data=entity_context,
                            headers={'Content-Type': 'text/plain'})
    if (response.status_code == 204):
        return 'Context updated'
    else:
        return 'Action failed'
