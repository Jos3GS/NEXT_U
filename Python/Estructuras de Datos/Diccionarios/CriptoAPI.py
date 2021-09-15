import requests
_API_KEY = "4f93b8c7-7aee-4df5-8e11-0a188fbf0ea2"

def esmoneda(cripto):
    return cripto in monedas

monedas=()
monedas_dict={}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': _API_KEY
}

data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
for cripto in data["data"]:
    monedas_dict[cripto["symbol"]]=cripto["name"]

monedas = monedas_dict.keys()

moneda=input("Indique el nombre de la moneda a verificar: ")
while not esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:",moneda,"y nombre:",monedas_dict.get(moneda),
          "es valida porque existe en coimnmarketcap.com")
