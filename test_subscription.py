"""

Usage::
    ./test_subscription.py [<id>] [<type>] [<attr>] [<url:port>]

Example: ./test_subscription.py T1 Termometer temperature http://host.docker.internal:1028 # noqa

"""

import sys
import json
from integration_modules.consult_subs import new_subscription
from sys import argv


print(sys.executable)
print(sys.version)

subscription_json = """{
    "description": "A subscription to get info about Room1",
    "subject": {
        "entities": [
            {
                "id": """+'"'+argv[1]+'"'+""",
                "type": """+'"'+argv[2]+'"'+"""
            }
        ],
        "condition": {
            "attrs": [
                """+'"'+argv[3]+'"'+"""
            ]
        }
    },
    "notification": {
        "http": {
            "url": """+'"'+argv[4]+'"'+"""
        },
        "attrs": [
            """+'"'+argv[3]+'"'+"""
        ]
    },
    "expires": "2040-01-01T14:00:00.00Z",
    "throttling": 5
}"""

parsed_json_subs = json.loads(subscription_json)

print(new_subscription(parsed_json_subs))
