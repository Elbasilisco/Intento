import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_ceros = 0
        maximo = 0
        minimo = 0
        seguir = True

        while True:
            numero = prompt("utrn", "ingrese numero")
            if numero == None:
                break

            while numero == " ": #or not numero.isdigit: #en este ejercicio no es necesario no sirve
                numero = prompt("utn", "ingrese numero")
            
            numero = int(numero)

            if numero < 0:
                acumulador_negativos += numero
                contador_negativos += 1
            elif numero == 0:
                contador_ceros += 1
            else:
                acumulador_positivos += numero
                contador_positivos += 1

            if (maximo and minimo) == 0:
                maximo = numero
                minimo = numero
            else:
                if numero > maximo:
                    maximo = numero
                elif numero < minimo:
                    minimo = numero
        diferencia = contador_positivos - contador_negativos
        if diferencia < 0:
            diferencia *= -1
            
        alert("informe", f"la suma acumulada de los negativos es: {acumulador_negativos}"+ "el max es "+ str(maximo) + " el min es "+ str(minimo))
        pass

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()