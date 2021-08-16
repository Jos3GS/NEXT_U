from datetime import datetime as dt
from datetime import timedelta as td

_simbolo = input("Ingrse la criptomoneda: ")
_acumulado = float(input("Ingrese la cantidad acumulada: "))
_cotizacion = float(input("Ingrese la cotizacion del dia: "))

_total_futuro = _acumulado + (_acumulado*5/100*7)
_dia_futuro = dt.now() + td(days=7)

print("La cantidad que posee al dia",dt.now().strftime("%A %d/%m/%Y")," es de",_acumulado,_simbolo,"O en USD$",_acumulado*_cotizacion)
print("La Cantidad que poseerá al dia",_dia_futuro.strftime("%A %d/%m/%Y"),"Será de",_total_futuro,_simbolo,"O en USD$",_total_futuro*_cotizacion)
print("Con Una ganancia de",_total_futuro-_acumulado,_simbolo,"O en USD$",_total_futuro*_cotizacion-_acumulado*_cotizacion)