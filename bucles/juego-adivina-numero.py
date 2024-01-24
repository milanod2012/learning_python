import random

print("bienvenido al juego")
numero_secreto= random.randint(1,100) #genera un nro. aleatorio entre 1 y 1000
intentos_max = 10 #cantidad de intentos que tiene el jugador para adivinar
intentos_realizados= 0

while intentos_realizados < intentos_max:
    intento = int(input("adivina el número secreto(entre 1 y 100): "))
    intentos_realizados += 1

    if intento == numero_secreto:
        print(f"!felicidades¡ adivinaste el numero en {intentos_realizados} intentos.")
        break
    elif intento < numero_secreto:
      
        print(f"el número es mayor. \n quedan {intentos_max-intentos_realizados} intentos: ")
    else:
    
        print(f"el número es menor. \nquedan {intentos_max-intentos_realizados} intentos: ")

if intentos_realizados == intentos_max:
    print("el juego termina! has perdido")