#diccionario1  = {"Nombre":"Elsa", "Edad": 39, "Nombre":"Ramon", "Edad": 62, "Nombre":"Saul", "Edad": 24}#esta retocado y las funciones son acorde a la anterior version
estudiantes = [{"Julian":{"Matematica": 9, "Lengua":5, "Fisica": 3}}, {"Sandra":{"Matematica": 4, "Lengua":7, "Fisica": 6}}, {"Sebastian":{"Matematica": 4, "Lengua":2, "Fisica": 10}}]
def mostrar_edad_diccionario(diccionario):
    persona = input("Ingrese el nombre de quien desea saber la edad: ")
    if persona in diccionario:
        respuesta = print(f"La edad de {persona} es {diccionario[persona]}")
        return respuesta
    else:
        print("No existe")
        return None

def alta_de_persona(diccionario):
    persona = input("Ingrese el nombrede la persona a dar de alta: ")
    if persona not in diccionario:
        edad = int(input("Ingrese la edad: "))
        diccionario[persona] = edad
        return True
    else:
        print("Ya existe ese nombre")
        return False    

def baja_de_persona(diccionario):
    persona = input("Ingrese el nombre de la persona a dar de baja: ")
    if persona in diccionario:
        diccionario.pop(persona)
        return True
    else:
        print("No se pudo eliminar persona inexistente")
        return False  
    
def calif_mas_alta(list_dicc):
    nombre = input("Ingrese el nombre del alumno: ")
    for i in range (len(list_dicc)):
        bandera = True
        if nombre in list_dicc[i]:
            for clave in list_dicc[i]:
                    for materia in list_dicc[i][clave]:
                        if bandera == True or list_dicc[i][clave][materia] > nota_mayor:
                            nota_mayor = list_dicc[i][clave][materia]
                            bandera = False
                    return nota_mayor
        else:
            if i == len(list_dicc):
                print("Ese alumno no existe")
                    
def promedio_notas(list_dicc):
    nombre = input("Ingrese el nombre del alumno: ")
    acumulador_notas = 0
    contador_notas = 0
    for i in range (len(list_dicc)):
        if nombre in list_dicc[i]:
            for clave in list_dicc[i]:
                    for materia in list_dicc[i][clave]:
                            acumulador_notas += list_dicc[i][clave][materia]
                            contador_notas += 1
                    promedio = acumulador_notas / contador_notas
                    return promedio
        else:
            if i == len(list_dicc):
                print("Ese alumno no existe")

#diccionario1.pop(24)     
print(promedio_notas(estudiantes))

"""print(estudiantes[0]["Julian"]["Lengua"])
if "Sebastian" in estudiantes[2]:
    print("existe")
else:
    print("no exixte")"""