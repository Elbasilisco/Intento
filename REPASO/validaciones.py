def es_primo(numero):
    numero = int(numero)
    if numero >= 2:
        for i in range(2, numero):
            if (numero ) % i == 0:
                return False

        return True
    else:
        return False
    
es_primo(25)