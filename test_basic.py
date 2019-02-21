import sys
import json
from integration_modules.insert_context import test_orion, put_entity
from integration_modules.insert_context import update_specific_atribute
from integration_modules.consult_query import get_entities, get_entities_filter
from integration_modules.consult_subs import new_subscription
from integration_modules.setup_address import set_address
from integration_modules.services_manager import get_entities_id_from_type
from integration_modules.services_manager import get_entities_info_from_id


print(sys.executable)
print(sys.version)

print(test_orion())

insert_entity = """{
                  "id": "T12",
                  "type": "Termometer12",
                  "temperature": {
                    "value": 24,
                    "type": "Float"
                  },
                  "pressure": {
                    "value": 620,
                    "type": "Integer"
                  }
                }"""

parsed_json = json.loads(insert_entity)

# print(put_entity(parsed_json))

entity_id1 = 'T1234'
entity_atribute1 = 'temperature'
entity_context1 = '32'

# Make the method able to update different types of information
# print(update_specific_atribute(entity_id1,
#                               entity_atribute1, entity_context1))

# print(get_entities())

list_of_filters = [["type", "=Store"],
                   ["georel", "=near;maxDistance:1500"],
                   ["geometry", "=point"],
                   ["coords", "=52.5162,13.3777"]]

# ["q=address.addressLocality", "==Kreuzberg"]

list_of_filters2 = [["q=temperature", ">12"]]

# print(get_entities_filter(list_of_filters2))

subscription_json = """{
                  "description": "A subscription to get info about Room1",
                  "subject": {
                    "entities": [
                      {
                        "id": "T1234",
                        "type": "Termometer"
                      }
                    ],
                    "condition": {
                      "attrs": [
                        "pressure"
                      ]
                    }
                  },
                  "notification": {
                    "http": {
                      "url": "http://localhost:1028/accumulate"
                    },
                    "attrs": [
                      "temperature"
                    ]
                  },
                  "expires": "2040-01-01T14:00:00.00Z",
                  "throttling": 5
                }"""

parsed_json_subs = json.loads(subscription_json)

# print(new_subscription(parsed_json_subs))

# list_of_ids = []
# list_of_ids = get_entities_id_from_type('Termometer')

# for x in list_of_ids:
#     print(x)

# get_entities_info_from_id('T12')
