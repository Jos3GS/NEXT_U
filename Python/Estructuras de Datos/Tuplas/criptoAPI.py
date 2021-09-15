import requests
_API_KEY = "4f93b8c7-7aee-4df5-8e11-0a188fbf0ea2"

def esmoneda(_cripto):
    return _cripto in _monedas
_monedas_list = []

headers = {'accepts':'application/json', 'X-CMC_PRO_API_KEY':_API_KEY}
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for _cripto in data["data"]:
    _monedas_list.append(_cripto["symbol"])

_monedas = tuple(_monedas_list)

_moneda = input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(_moneda):
    print("Moneda Invalida.")
    _moneda=input("Indique el nombre de la moneda: ")
else:
    print("La Moneda ",_moneda,"Es valida porque existe en coinmarketcap.com")