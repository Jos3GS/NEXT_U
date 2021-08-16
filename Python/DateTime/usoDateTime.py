from datetime import datetime as dt

_simbolo = input("Ingrese la criptomoneda: ")
_cantidad = float(input("Ingrese la cantidad acumulada: "))
_cotizacion = float(input("Ingrese la cotizacion de 1 "+_simbolo+"= a X USD: "))

print("Tienes",_cotizacion*_cantidad,"USD de",_simbolo)
print("Esta informacion fue obtenida el: ",dt.now().strftime("%A %d/%m/%Y %I:%M:%S %p"))