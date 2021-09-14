_List_moneda = []
_n = 3

for i in range(0,5):
    _List_moneda.append([])
    _List_moneda[i].append(input("Ingrese el Nombre de la Moneda:    "))
    _List_moneda[i].append(float(input("Ingrese El Saldo que tiene:  ")))
    _List_moneda[i].append(float(input("Ingrese la Cotización:       ")))

for i in range(0,len(_List_moneda)):
    for j in range(0,_n):
        print(_List_moneda[i][j])
    print("--------------------------")
    