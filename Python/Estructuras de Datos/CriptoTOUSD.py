_Arr_Cripto = []
_m = 5
_n = 3
_suma = 0

for i in range(0,_m):
    _Arr_Cripto.append([])
    _Arr_Cripto[i].append(input("Ingrese el Nombre de la Moneda:    "))
    _Arr_Cripto[i].append(float(input("Ingrese El Saldo que tiene:  ")))
    _Arr_Cripto[i].append(float(input("Ingrese la Cotización:       ")))

for i in range(0,_m):
    for j in range(0,_n):
        print(_Arr_Cripto[i][j])
    print("--------------------------")
    

for i in range(0,_m):
    _suma = _suma + (_Arr_Cripto[i][1]*_Arr_Cripto[i][2])

print("Cantidad Total en USD es: ",_suma)