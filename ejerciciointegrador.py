alumnos = []

while True:
    print("\nIngrese el número de la operación que desea ejecutar:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Salir.")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        if alumnos:
            print("Lista de alumnos:")
            for alumno in alumnos:
                print(f"Nombre: {alumno[0]}, Cursos: {alumno[1]}")
        else:
            print("No hay alumnos ingresados.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ")
        cursos = int(input("Ingrese la cantidad de cursos en los que está inscripto: "))
        alumnos.append([nombre, cursos])
        print("Alumno ingresado correctamente.")
    elif opcion == "3":
        print("¡Gracias por utilizar el programa!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
