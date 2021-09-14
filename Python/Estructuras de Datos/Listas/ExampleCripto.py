import requests
_ENDPOINT = "https://api.binance.com"

def _url(api):
    return _ENDPOINT+api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda(cripto):
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    return cripto in criptos

def esnumero(numero):
    return numero.replace(".","",1).isdigit()

_monedas=[]
_cantidades=[]
_cotizaciones=[]

i=0
while i<3:
    _moneda=input("Ingrese el nombre de la moneda: ")
    while not esmoneda(_moneda):
        print("Moneda Invalida.")
        _moneda=input("Ingrese el nombre de la moneda: ")
    else:
        _monedas.append(_moneda)
        data = get_price(_moneda+"USDT").json()
        _cotizaciones.append(float(data["price"]))
        _cantidad = input("Ingrese la cantidad: ")
        while not esnumero(_cantidad):
            _cantidad = input("Ingrese la cantidad: ")
        else:
            _cantidades.append(float(_cantidad))
    i+=1

i=0
total=0

while i<3:
    total+=_cantidades[i]*_cotizaciones[i]
    print("Moneda: ",_monedas[i],
        ", Cantidad: ",_cantidades[i],
        ", Cotizacion de USDT: ",_cantidades[i]*_cotizaciones[i])
    i+=1
print("Total en USDT es: ",str(total))