def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0 and año % 400 != 0:
            print("no es bisiesto")
            return False
        print("es bisiesto")
        return True
        
    else:
        print("no es")
        return False
    
es_bisiesto(2024)