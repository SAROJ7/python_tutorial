import json
from urllib.request import urlopen

usd_rates = {}
with urlopen("https://api.currencyfreaks.com/latest?apikey=05fb9166f86841248d5d1a9fa5c82b6f") as response:
    source = response.read()

print(source)

data = json.loads(source)

print(json.dumps(data, indent=2))

# print(f'The value of 1 dollar is {data["rates"]["NPR"]} npr')
usd_rates = data["rates"]
print(usd_rates)

with open('currency.json', 'w') as f:
    json.dump(data["rates"], f, indent=2)