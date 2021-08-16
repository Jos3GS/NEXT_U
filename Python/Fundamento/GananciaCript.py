_nombre, _cantidad = input("Ingrese el Nombre de la Criptomoneda: "), float(input("Ingrese la cantidad: "))
_dias_negocio, _ganancia_dia = int(input("Ingrese los dias negociados: ")), float(input("Ingrese la Ganancia por dia en %: "))

_ganancia = _cantidad*_ganancia_dia/100*_dias_negocio
_ganancia_total = _cantidad+_ganancia

print("Despues de",_dias_negocio,"Ha ganado",_ganancia,_nombre,"Quedando con un total de",_ganancia_total,_nombre)