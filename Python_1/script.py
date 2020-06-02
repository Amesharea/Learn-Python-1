import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

r = requests.get('https://google.de')
print(r.status_code)

name = input("Your Name? ")
print("Hello,", name)

