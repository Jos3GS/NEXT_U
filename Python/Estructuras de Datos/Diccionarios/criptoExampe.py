import requests
def esmoneda(_cripto):
    return _cripto in _monedas
_API_KEY = "4f93b8c7-7aee-4df5-8e11-0a188fbf0ea2"
_monedas =()
_monedas_dict={}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': _API_KEY
}

_data = requests.get("https://api.coinmarketcap.com/v2/ticker/",headers=headers).json()
for id in _data["data"]:
    _monedas_dict[_data["data"][id]["symbol"]]=_data["data"][id]["quotes"]["USD"]["price"]

_monedas=_monedas_dict.keys()

_moneda = input("Ingrese el nombre de la monea: ")
while not esmoneda(_moneda):
    print("Moneda Invalida.")
    _moneda=input("INgrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:",_moneda,"Tiene un precio de:",_monedas_dict.get(_moneda),"USD")
