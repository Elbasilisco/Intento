import os
estudiantes = [{"Legajo": 100000, "Nombre": "Julian", "Apellido": "Silva", "Calificaciones":{"Matematica": 2, "lengua": 3, "Fisica": 8}}, 
               {"Legajo": 100001, "Nombre": "Silvia", "Apellido": "Colman", "Calificaciones":{"Matematica": 4, "lengua": 8, "Fisica": 10}},
               {"Legajo": 100002, "Nombre": "Ester", "Apellido": "Zanetti", "Calificaciones":{"Matematica": 9, "lengua": 7, "Fisica": 6}},
               {"Legajo": 100002, "Nombre": "Carlitos", "Apellido": "Bala", "Calificaciones":{"Matematica": 4, "lengua": 7, "Fisica": 3}}]

def alta_alumno(nombre, apellido):
    #nombre = input("Ingrese un nombre: ")
    #apellido = input("Ingrese un apellido: ")
    ultimo_legajo = estudiantes[len(estudiantes)-1]["Legajo"]
    for i in range (len(estudiantes)):
        print(i)
        if nombre in estudiantes[i]["Nombre"] and apellido in estudiantes[i]["Apellido"]:
            print("Ese alumno ya existe")
        else:
            if i == len(estudiantes) - 1:
                estudiantes.append({"Legajo": ultimo_legajo + 1, "Nombre": nombre, "Apellido": apellido, "Calificaciones":{"Matematica": -1, "lengua": -1, "Fisica": -1}})

def menu(lista):
    for i in range (len(lista)):
        print(f"{i} {lista[i]}")
    opcion = input("Elija una opcion: ")
    return opcion

def cambiar_nombre(legajo):
    for i in range (len(estudiantes)):
        if legajo in estudiantes[i]["Legajo"]:
            cambio = input("Ingrese el nuevo nombre: ")
            estudiantes[i]["Nombre"] = cambio
        else:
            if i == len(estudiantes) - 1:
                print("Ese legajo no existe")

def cambiar_apellido(legajo):
    for i in range (len(estudiantes)):
        if legajo in estudiantes[i]["Legajo"]:
            cambio = input("Ingrese el nuevo apellido: ")
            estudiantes[i]["Apellido"] = cambio
        else:
            if i == len(estudiantes) - 1:
                print("Ese legajo no existe")

def cambiar_materia(legajo):
    for i in range (len(estudiantes)):
        if legajo == estudiantes[i]["Legajo"]:
            print(estudiantes[i]["Calificaciones"])
            materia = input("Cual materia desea cambiar:")
            del (estudiantes[i]["Calificaciones"][materia])
            cambio = input("Ingrese la nueva materia: ")
            nota = input("Ingrese la nota de la nueva materia: ")
            estudiantes[i]["Calificaciones"][cambio] = nota
        else:
            if i == len(estudiantes) - 1:
                print("Ese legajo no existe")

def cambiar_nota(legajo):
    for i in range (len(estudiantes)):
        if legajo == estudiantes[i]["Legajo"]:
            print(estudiantes[i]["Calificaciones"])
            materia = input("De cual materia desea cambiarla nota:")
            nota = input("Ingrese la nueva nota de la materia: ")
            estudiantes[i]["Calificaciones"][materia] = nota
        else:
            if i == len(estudiantes) - 1:
                print("Ese legajo no existe")
                
def modificar_alumno(legajo):
    while True:
        menu(["Nombre", "Apellido", "Materias", "Calificaciones"])
        os.system("cls")
        match(menu):
            case 0:
                cambiar_nombre(legajo)
            case 1:
                cambiar_apellido(legajo)
            case 2:
                cambiar_materia(legajo)
            case 3:
                cambiar_nota(legajo)
            case _:
                break

def mostrar_nombre_completo(lst_dicc):
    for i in range (len(estudiantes)):
        print(f"[{i}] {estudiantes[i]["Nombre"]}\t{estudiantes[i]["Apellido"]}")

def nota_mas_baja_de_materia(lst_dicc):
    materia = input("Cual es la materia de la cual desea saber la nota mas baja: ")
    bandera = True
    for i in range(len(estudiantes)):
        for j in estudiantes[i]["Calificaciones"]:
            if materia == j:
                if bandera == True or estudiantes[i]["Calificaciones"][materia] < menor_nota:
                    menor_nota = estudiantes[i]["Calificaciones"][materia]
                    bandera = False
    return menor_nota

def lista_alfabetica():
    #for a in range(len(estudiantes)):
        for i in range(len(estudiantes)-1):
            # Recorro el resto de los elementos para comparar cuales cumplen el criterio
            # de ordenamiento 
            for j in range( i+1, len(estudiantes)):
                # Si los elementos no estan ordenados, los intercambio
                if estudiantes[i]["Apellido"] > estudiantes[j]["Apellido"]:
                    #(lista[i], lista[j]) = (lista[j], lista[i]) #No funciona en la mayoria de los lenguajes
                    aux = estudiantes[i]["Apellido"]
                    estudiantes[i]["Apellido"] = estudiantes[j]["Apellido"]
                    estudiantes[j]["Apellido"] = aux

letras = ["f", "g", "j", "a", "e", "c"]

print(lista_alfabetica())
for i in estudiantes:
    print(i)