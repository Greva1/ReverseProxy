#test load-balance

import requests

while 1:
    r = requests.get("http://localhost:8080/")
    print(r)
