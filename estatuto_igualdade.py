import requests


API_ENDPOINT = "https://dre.pt/home/-/dre/feed/exclusive/1/cacheLevelPage?serie=II&parte=C"

r = requests.get(url = API_ENDPOINT)

print(r.text)

