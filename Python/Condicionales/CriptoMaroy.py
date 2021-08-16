_simbolo1 = input("Ingrese en Simbolo de la Primera Criptomoneda: ")
_simbolo2 = input("Ingrese en Simbolo de la Segunda Criptomoneda: ")
_simbolo3 = input("Ingrese en Simbolo de la Tercera Criptomoneda: ")

_cantidad1 = float(input("Ingrese la cantidad de "+_simbolo1+": "))
_cantidad2 = float(input("Ingrese la cantidad de "+_simbolo2+": "))
_cantidad3 = float(input("Ingrese la cantidad de "+_simbolo3+": "))

if _cantidad1 > _cantidad2 and _cantidad1 > _cantidad3:
    print(_simbolo1,_cantidad1)
    if _cantidad2 > _cantidad3:
        print(_simbolo2,_cantidad2)
        print(_simbolo3,_cantidad3)
    else:
        print(_simbolo3,_cantidad3)
        print(_simbolo2,_cantidad2)
elif _cantidad2 >_cantidad1 and _cantidad2 >_cantidad3:
    print(_simbolo2,_cantidad2)
    if _cantidad1 > _cantidad3:
        print(_simbolo1,_cantidad1)
        print(_simbolo3,_cantidad3)
    else:
        print(_simbolo3,_cantidad3)
        print(_simbolo1,_cantidad1)
elif _cantidad3 >_cantidad1 and _cantidad3 > _cantidad2:
    print(_simbolo3,_cantidad3)
    if _cantidad1 > _cantidad2:
        print(_simbolo1,_cantidad1)
        print(_simbolo2,_cantidad2)
    else:
        print(_simbolo2,_cantidad2)
        print(_simbolo1,_cantidad1)
else:
    print("Lo dañaste bro xd")