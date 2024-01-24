#funcion que suma los argumentos 
def sumar(*args, **kargs):
    suma=0
    for n in args:
        suma += n
        return suma,kargs
suma_T, datos= sumar(10,15,101, nombre='daniel', edad=25)
print('la suma de todos los argumentos',suma_T)
print(datos)