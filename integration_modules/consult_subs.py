# Performs subscription requests to the Orion Context Broker

import requests
from integration_modules.setup_address import set_address

address = set_address()


def new_subscription(detailed_subs):
    url = 'http://'+address+':1026/v2/subscriptions'

    response = requests.post(url, json=detailed_subs)

    if (response.status_code == 201):
        return 'Subscription done. Subs ID: '+response.headers['Location']
    else:
        return 'Subscription failed'
