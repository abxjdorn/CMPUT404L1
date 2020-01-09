import requests

print(requests.__version__)

print(requests.get('http://www.google.com/').text)

print(requests.get('https://raw.githubusercontent.com/abxjdorn/CMPUT404L1/master/L1.py').text)
