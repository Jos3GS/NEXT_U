_total = 0.0
i = 0

while i <5:
    _nombre = input("Ingrese el Nombre de la Moneda: ")
    _cantidad = float(input("Ingrese la cantidad: "))
    _cotizacion = float(input("Ingrese la cotizacion en USD de la moneda: "))
    _total = _total + _cantidad*_cotizacion
    i = i+1

print("Usted tiene en total",_total,"USD")


