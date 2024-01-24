mi_diccionario = {}
#Agregar un par clave-valor a la diccionario.   
mi_diccionario = {'nombre' : 'juan', 'edad' : '30', 'ciudad' : 'caracas'}

print(mi_diccionario['nombre'])
#Acceder a los valores de una llave específica en el diccionario.
for i in mi_diccionario:
    print("%s:%s" % (i, mi_diccionario[i]))


#iterar 
    
for y,i in mi_diccionario.items():
       print(y,i)
