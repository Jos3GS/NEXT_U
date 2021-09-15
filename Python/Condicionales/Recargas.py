BTCUSD=7630.80
DASHUSD=315.56
LTCUSD=120.84

_simbolo = input("Eliga con que moneda va a realizar la recarga (BTC, DASH, LTC): ")
if _simbolo.upper() == "BTC":
    _monto = float(input("Ingrese el Monto a recargar: "))
    print("la recarga por",_monto*BTCUSD,"USD Ha sido Exitosa")
elif _simbolo.upper() == "DASH":
    _monto = float(input("Ingrese el Monto a recargar: "))
    print("la recarga por",_monto*DASHUSD,"USD Ha sido Exitosa")
elif _simbolo.upper() == "LTC":
    _monto = float(input("Ingrese el Monto a recargar: "))
    print("la recarga por",_monto*LTCUSD,"USD Ha sido Exitosa")
else:
    print("La recarga no se puede realizar en esta moneda")