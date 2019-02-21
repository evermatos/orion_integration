# Works alongisde with the context_manager to provide services based on the context present at the broker # noqa

import requests
from integration_modules.setup_address import set_address


address = set_address()


def get_entities_types():
    url = 'http://'+address+':1026/v2/types?options=values'
    response = requests.get(url)

    if (response.status_code == 200):
        list_of_types = []
        for x in response.json():
            list_of_types.append(x)
        return list_of_types
    else:
        return 'Query failed'


def get_entities_id_from_type(entity_type):
    url = 'http://'+address+':1026/v2/entities?options=keyValues&type=' + entity_type  # noqa
    response = requests.get(url)

    if (response.status_code == 200):
        list_of_ids = []
        for x in response.json():
            list_of_ids.append(x["id"])
        return list_of_ids
    else:
        return 'Query failed'


def get_entities_info_from_id(entity_id):
    url = 'http://'+address+':1026/v2/entities/'+entity_id+'/attrs?options=keyValues'  # noqa
    response = requests.get(url)

    if (response.status_code == 200):
        list_of_context = []
        for x in response.json():
            list_of_context.append(x)
        return list_of_context
    else:
        return 'Query failed'
