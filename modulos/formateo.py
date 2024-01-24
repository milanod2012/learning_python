from sys import argv


if len(argv) ==4:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])
   
   #TIPOS DE FORMATEO EN PRINT 
    #print(f'Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}')
    #print('Nombre: {} \nEdad: {} \nAltura: {}'.format(nombre,edad,altura))
    #print('Nombre: {n} \nEdad: {e} \nAltura: {a}'.format(a=altura, e= edad, n=nombre))
    print('Nombre: %s \nEdad: %i \nAltura: %f'%(nombre,altura,edad) )

    
    

else:
    print("error ingrese los argumentos")
    print('ejemplo: formateo.py "texto" 25 1.67 ')
