#Al ejercicio de alumnos* que se había creado en la versión anterior del proyecto integrador, que se resolvió con un diccionario, 
# ahora le debe agregar funciones para que verifique los datos y tratar de organizar mejor para poder aprovechar la reutilización de código.


def es_numero_valido(cadena):
    # Tiene que ser solo dígitos
    for caracter in cadena:
        if caracter < '0' or caracter > '9':
            return False
    return True


alumnos = {}

while True:
    print("\nIngrese el número de la opcion que desea:")
    print("1 - Ver la lista de alumnos.")
    print("2 - Añadir un alumno a la lista.")
    print("3 - Ver la cantidad de cursos de un alumno.")
    print("4 - Salir.")
    
    opcion = input("Opción ingresada: ")
    
    if opcion == "1":
        if alumnos:
            print("Lista de alumnos:")
            for nombre, cursos in alumnos.items():
                print(f"Nombre: {nombre}, Cursos: {cursos}")
        else:
            print("No hay alumnos ingresados.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre del alumno: ").strip() # la funcion strip ayuda a que no se ingrese con espacios, borra espacios
        while nombre in alumnos or len(nombre) == 0:
            if nombre in alumnos:
                print("Error! El alumno ya está ingresado. Ingrese un nombre diferente.")
            elif len(nombre) == 0:
                print("Error! El nombre no puede estar vacío. Ingrese un nombre válido.")
            nombre = input("Ingrese el nombre del alumno: ").strip()

        cursos = input("Ingrese la cantidad de cursos en los que está inscrito: ")
        while not es_numero_valido(cursos):
            print("Por favor, ingrese un número válido.")
            cursos = input("Ingrese la cantidad de cursos en los que está inscrito: ")
        
        alumnos[nombre] = int(cursos)
        print("El alumno due ingresado correctamente.")
    
    elif opcion == "3":
         print("Ver la cantidad de cursos de un alumno.")
         nombre = input("Ingrese el nombre del alumno: ")
         if nombre in alumnos:
             print("El alumno {} tiene {} cursos.".format(nombre, len(alumnos[nombre])))
             
         else:
             print("El alumno no existe en la lista.")
    
    elif opcion == "4":
        print("¡Gracias por utilizar mi programa!")
        break
    
    else:
        print("Error!! Opcion no valida, vuelva a intentarlo.")


