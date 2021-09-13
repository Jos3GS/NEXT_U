_Arr_Cripto = []
_m = 5
_n = 3

for i in range(0,_m):
    _Arr_Cripto.append([])
    _Arr_Cripto[i].append(input("Ingrese el Nombre de la Moneda:    "))
    _Arr_Cripto[i].append(float(input("Ingrese El Saldo que tiene:  ")))
    _Arr_Cripto[i].append(float(input("Ingrese la Cotización:       ")))

for i in range(0,_m):
    for j in range(0,_n):
        print(_Arr_Cripto[i][j])
    print("--------------------------")
    