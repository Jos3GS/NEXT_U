_nombre_archivo = input("Ingrese el nombre del archivo a analizar")
_archivo= open(_nombre_archivo,"r")

_texto = _archivo.read()
_palabras = _texto.split()
_ocurrencia = {}

for _palabra in _palabras:
    if _ocurrencia.get(_palabra):
        _ocurrencia[_palabra]+=1
    else:
        _ocurrencia[_palabra]=1
    
maxpar=None, 0
for _palabra, _cantidad in _ocurrencia.items():
    if maxpar[1]<_cantidad:
        maxpar=_palabra,_cantidad
print("La Palabra con mayor cantidad de repeticiones es",maxpar[0],"Repetida",maxpar[1],"Veces")
