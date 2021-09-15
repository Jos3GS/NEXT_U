_nombre_archivo = input("Ingrese el nombre del archivo: ")
_archivo = open(_nombre_archivo)
_dicionario = {}
_lineas = _archivo.readlines()
for _linea in _lineas:
    _definicion = _linea.split(":")
    _dicionario[_definicion[0]]=_definicion[1]

_palabra = input("Ingrese la palabra a buscar: ")

if _dicionario.get(_palabra) != None:
    print(_dicionario.get(_palabra))
else:
    _sn = input("Esta palabra au no esta en el diccionario, ¿Desea Agregarla? (s) o (n) ")
    if _sn  == "s" or _sn == "S":
        _definicion = input("Ingrese la definicion: ")
        _dicionario[_palabra] = _definicion

_archivo.writelines(_dicionario)
