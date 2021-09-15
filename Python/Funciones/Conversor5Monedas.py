def ConvertirUSD():
    _simbolo = input("Escriba la moneda a ingresar: ")
    _cantidad = float(input("Ingrese la cantidad de la Moneda: "))
    _cotizacion = float(input("Ingrese la cotizacion de la Moneda: "))
    _total = _cantidad*_cotizacion
    return _total

i = 0
_valor = 0.0
while i < 5:
    _valor = _valor + ConvertirUSD()
    i = i + 1

print("Usted tiene",_valor,"Dolares")