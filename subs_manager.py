# Receives the subscription intention (from users) and creates the process

from integration_modules.services_manager import get_entities_id_from_type
from integration_modules.services_manager import get_entities_info_from_id
from integration_modules.services_manager import get_entities_types


list_of_types = get_entities_types()

print('Types of context present at Orion Context Broker:')
for x in list_of_types:
    print(x)

for y in list_of_types:
    print('')
    print('The type "'+y+'" has the following entities (id): ')
    list_of_entities = get_entities_id_from_type(y)
    print(list_of_entities)
    print('')
    for z in list_of_entities:
        print('The entity "'+z+'" has the following context information: ')
        list_of_context = get_entities_info_from_id(z)
        print(list_of_context)
