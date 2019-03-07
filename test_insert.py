import sys
import json
from integration_modules.insert_context import put_entity


print(sys.executable)
print(sys.version)

insert_entity = """{
                  "id": "T3",
                  "type": "Termometer",
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

print(put_entity(parsed_json))
