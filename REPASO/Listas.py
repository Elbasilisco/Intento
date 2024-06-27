from mi_paquete._utilidades import *
lista_1_a_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mostrar_lista_por_item(lista):
    for item in lista:
        print(item)

def modificar_item_de_lista(lista):
    print(lista)
    item_a_modificar = int(input(f"Seleccione que item de la lista desea modificar desde el indice 0 al {len(lista)-1}:"))
    lista[item_a_modificar] = input("Ingrese el nuevo valor del item\n")
    return lista

def agregar_item_a_lista(lista):
    preferencia = input("Desea ingresarlo en una posicion en particular de la lista? s/n\n")
    if preferencia == "s":
        indice = int(input(f"Seleccione el indice al que desea añadir el item desde 0 al {len(lista)-1}:"))
        #lista[indice:indice + 1]= (input("Añada el nuevo item: ")), lista[indice]
        lista.insert(indice, (input("Añada el nuevo item: ")))
    else:
        lista.append(input("Añada el nuevo item: "))
    return lista

def mostrar_rango_de_lista(lista):
    print(lista)
    rango1 = int(input(f"Ingrese el indice desde el cual mostar el rango de lista, debe ser menor a {len(lista)-1}: "))
    rango2 = int(input(f"Ingrese el indice hasta el cual mostar el rango de lista, maximo {len(lista)-1}: "))
    print(lista[rango1:rango2])

def eliminar_1er_ocurrencia_de_lista(lista):
    ocurrencia = int(input("Ingrese valor del item del cual desea eliminar la 1ra ocurrencia: "))
    #for i in lista:
    lista.remove(ocurrencia)
    print(lista)
    return lista
    
def vaciar_lista(lista):
    lista.clear()
    print(lista)
    return lista

lista2 = ["awa", "ewe", "iwi", "owo", "uwu"]
lista3 = [69, "ñ", "lel", 42, 420]

lista_nueva = [lista_1_a_10, lista2, lista3]

def juntar_listas(lista1, lista2, lista3 = None, lista4 = None, lista5 = None):
    nueva_lista = lista1 + lista2

def mostrar_lista_por_subitem(lista_con_listas):
    for item in lista_con_listas:
        for sub_i in item:
            print(sub_i)

def modificar_subitem_de_lista(lista):
    print(lista)
    seleccionar_lista = int(input(f"Seleccione que lista desea modificar desde 0 al {len(lista)-1}:"))
    print(lista[seleccionar_lista])
    item_a_modificar = int(input(f"Seleccione que subitem de la lista desea modificar desde el indice 0 al {len(lista[seleccionar_lista])-1}:"))
    lista[seleccionar_lista][item_a_modificar] = input("Ingrese el nuevo valor del item\n")
    return lista

def agregar_subitem_a_lista(lista):
    preferencia = input("Desea ingresarlo en una posicion en particular de la lista? s/n\n")
    if preferencia == "s":
        indice = int(input(f"Seleccione la lista desde 0 al {len(lista)-1}:"))
        print(lista[indice])
        sub_i = int(input(f"Seleccione el subindice al que desea añadir el item desde 0 al {len(lista[indice])}:"))
        #lista[indice:indice + 1]= (input("Añada el nuevo item: ")), lista[indice]
        lista[indice].insert(sub_i, (input("Añada el nuevo item: ")))
    else:
        lista.append([input("Añada el nuevo item: ")])
    return lista

def mostrar_subrango_de_lista(lista):
    print(lista)
    menu = int(input("[1] Mostrar rango de lista principal\n[2] Mostar rango de lista dentro de lista\nOpcion: "))
    match(menu):
        case 1:
            rango1 = int(input(f"Ingrese el indice desde el cual mostar el rango de lista, debe ser menor a {len(lista)-1}: "))
            rango2 = int(input(f"Ingrese el indice hasta el cual mostar el rango de lista, maximo {len(lista)}: "))
            print(lista[rango1:rango2])
        case 2:
            sublista = int(input(f"Seleccione una lista desde 0 a {len(lista)-1}: "))
            rango1 = int(input(f"Ingrese el indice desde el cual mostar el rango de lista, debe ser menor a {len(lista)-1}: "))
            rango2 = int(input(f"Ingrese el indice hasta el cual mostar el rango de lista, maximo {len(lista)-1}: "))
            print(lista[sublista][rango1:rango2])

def eliminar_1er_ocurrencia_de_sublista(lista):
    print(lista)
    ocurrencia = int(input("Ingrese el valor del item del cual desea eliminar la 1ra ocurrencia: "))
    for i in range (len(lista)):
        print(i)
        for s_i in range (len(lista[i])):
            print(s_i)
            if ocurrencia == lista[i][s_i]:
                lista[i].remove(ocurrencia)
                print(lista)
                return lista
            else:
                pass
    
def quitar_toda_subocurrencia_de_lista(lista):
    lista.clear()
    print(lista)
    return lista
#lista_nueva[0].remove(7)
eliminar_1er_ocurrencia_de_sublista(lista_nueva)
print(lista_nueva)

