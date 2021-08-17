_numero = int(input("Ingrese un numero: "))
_salida =""

if _numero%3==0:
    _salida+="Fizz"
if _numero%5==0:
    _salida+="Buzz"
if _salida == "":
    _salida+= str(_numero)

print(_salida)