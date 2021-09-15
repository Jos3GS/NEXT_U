_USD  = 0
_COTI = 0
_CANTCRIPTO = 0
_CRIPTO =""

_CRIPTO = input("Ingrese el Simbolo de la Cirpto-Moneda:  ")
_COTI = float(input("Ingrese la Contizacion de la Moneda 1 "+_CRIPTO+" = X USD, X es el valor a ingresar:  "))
_CANTCRIPTO = float(input("Ingrese la Cantidad en Criptomoneda que posee:  "))

_USD = _COTI * _CANTCRIPTO

print("Usted Posee un total de US$:  "+str(_USD))