#lista vacia para registro de estudiantes
registro_estudiantes = []

#menu principal
while True:
    print("1. Registrar Estudiante")
    print("2. Mostrar Registro")
    print("3. Salir")
    
    
    opcion = input("Ingrese una Opción: ")
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = int(input("Edad del estudiante: "))
        curso = input("Curso del estudiante: ")

        #crear un diccionario con los datos del estudiante y agregarlos
        estudiante = {'Nombre': nombre, 'Edad': edad, 'Curso':curso}
        registro_estudiantes.append(estudiante)

        print("estudiante registrado satisfactoriamente \n")


        
    elif opcion == "2":
       #mostrar registro
        if registro_estudiantes:
            print("\nRegistros de Estudiantes\n")
            for estudiante in registro_estudiantes:
                print(f"Nombre: {estudiante['Nombre']}, Edad:{estudiante['Edad']}, Curso: {estudiante['Curso']}")
                print()
        else:
            print("No hay ningun registro")
    elif opcion == "3":
        #salir del programa
        print("Saliendo del programa... !hasta luego¡ \n")
        break

    else:
        print("Opción Incorrecta, Por favor ingrese una opción válida. \n")



