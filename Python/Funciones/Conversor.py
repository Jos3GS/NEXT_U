def ConversionCriptomoneda(cantBTC, cantXRP):
    _BTCUSD = 7442.50
    _XRPUSD = 0.660982

    _saldo_total = cantBTC*_BTCUSD + cantXRP*_XRPUSD
    return _saldo_total

_cantBTC =float(input("Ingrese la Cantidad de BTC: "))
_cantXRP = float(input("Ingrese la cantidad de XRP: "))

print("LA caltidad total de USD$ es de:",ConversionCriptomoneda(_cantBTC,_cantXRP))