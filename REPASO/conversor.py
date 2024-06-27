def convertir_decimal_a_binario(numero):
    lista_numeros = ""
    while numero > 1:
        #numero = int(numero)
        #numero = numero % 2
        lista_numeros += str(numero % 2)
        numero = numero // 2

    lista_numeros += str(numero)
    lista_numeros = list(lista_numeros)
    lista_numeros.reverse()
    print(f"El numero pasado a binaro es: {lista_numeros}")

convertir_decimal_a_binario(10)

def convertir_binario_a_decimal(numero_binario):
    aux = list(numero_binario)
    potencia = len(numero_binario) - 1
    numero_decimal = 0
    for i in range(len(aux)):
        if aux[i] == "1":
            numero_decimal += 2 ** potencia
        potencia -= 1
    return numero_decimal

    