import sys
from integration_modules.consult_query import get_entities, get_entities_filter


print(sys.executable)
print(sys.version)


print(get_entities())

list_of_filters = [["type", "=Store"],
                   ["georel", "=near;maxDistance:1500"],
                   ["geometry", "=point"],
                   ["coords", "=52.5162,13.3777"]]

# ["q=address.addressLocality", "==Kreuzberg"]

list_of_filters2 = [["q=temperature", ">21"]]

print(get_entities_filter(list_of_filters2))
