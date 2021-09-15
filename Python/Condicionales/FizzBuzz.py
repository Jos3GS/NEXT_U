_numero = int(input("Ingrese el numero: "))

if _numero%3== 0 and _numero%5== 0:
    print("FizzBuzz")
elif _numero%3 == 0:
    print("Fizz")
elif _numero%5==0:
    print("Buzz")
else:
    print(_numero)