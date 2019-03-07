"""

Usage::
    ./test_update.py [<id>] [<attr>] [<new_context>]

Example: ./test_update.py T1 temperature 32

"""

import sys
from integration_modules.insert_context import update_specific_atribute
from sys import argv

print(sys.executable)
print(sys.version)

# Make the method able to update different types of information
print(update_specific_atribute(argv[1], argv[2], argv[3]))
