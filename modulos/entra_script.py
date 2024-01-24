# se utiliza para ingresar los atributos

import sys
if len(sys.argv) ==3:
    texto = sys.argv[1]
    cantidad = int(sys.argv[2])

    c= 0
    while c < cantidad:
        print(texto)
        c += 1
#print(sys.argv)
    
else:
    print("error ingrese los argumentos")
    print('ejemplo: entra_script.py "texto" 5 ')
