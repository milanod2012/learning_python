def saludar(nombre, edad):
    print(f"Hola, {nombre} y tu edad {edad}")
saludar("alex", 25) #tambien puede ser : saludar(edad=25, nombre="juan")
def suma(*args):
    return sum(args)

print(f"la suma es: {suma(10,10,10,10,10,10)}")

#**kwargs va a admitir varios argumentos al parametro
def otra_funcion(**kwargs):
    print(kwargs)

funct = otra_funcion(a = 'A', b= 'text', c= 45) #arroja un diccionario con los argumentos
print(funct)
#------------------------------
# si son argumentos indefinidos (**kwargs) va a arrojar un diccionario
# si los parametros estan definidos va a arrojar tupla

