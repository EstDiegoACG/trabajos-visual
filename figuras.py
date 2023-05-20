import math
from tkinter import *

def calcular_area_perimetro():
    figura = figura_var.get()

    if figura == "Círculo":
        
        radio = float(radio_entry.get())
        area = math.pi * radio**2
        perimetro = 2 * math.pi * radio
        
    elif figura == "Rectángulo":
        
        base = float(base_entry.get())
        altura = float(altura_entry.get())
        area = base * altura
        perimetro = 2 * (base + altura)
        
    elif figura == "Cuadrado":
        
        lado = float(lado_entry.get())
        area = lado**2
        perimetro = 4 * lado
        
    elif figura == "Triángulo":
        
        base = float(base_entry.get())
        altura = float(altura_entry.get())
        area = (base * altura) / 2
        perimetro = base + 2 * math.sqrt((base/2)**2 + altura**2)
        
    elif figura == "Rombo":
        
        diagonal_mayor = float(diagonal_mayor_entry.get())
        diagonal_menor = float(diagonal_menor_entry.get())
        area = (diagonal_mayor * diagonal_menor) / 2
        perimetro = 4 * math.sqrt(((diagonal_mayor/2)**2) + ((diagonal_menor/2)**2))
        
    elif figura == "Trapecio":
        
        base_mayor = float(base_mayor_entry.get())
        base_menor = float(base_menor_entry.get())
        altura = float(altura_entry.get())
        area = ((base_mayor + base_menor) * altura) / 2
        perimetro = base_mayor + base_menor + (2 * math.sqrt(((base_mayor - base_menor)/2)**2 + altura**2))
    
    elif figura == "Hexágono":
    
        lado = float(lado_entry.get())
        area = (3 * math.sqrt(3) * lado**2) / 2
        perimetro = 6 * lado
    
    else:
    
        area = 0
        perimetro = 0

    area_label.configure(text=f"Área: {area:.2f}")
    perimetro_label.configure(text=f"Perímetro: {perimetro:.2f}")

# Crear la ventana principal
window = Tk()
window.title("Calculadora de áreas y perímetros")
window.geometry("500x500")

# Variables para almacenar las opciones seleccionadas
figura_var = StringVar()
figura_var.set("Círculo")

# Etiqueta y cuadro de entrada para el radio del círculo
radio_label = Label(window, text="Radio: o")
radio_label.pack()
radio_entry = Entry(window)
radio_entry.pack()

# Etiqueta y cuadro de entrada para la base del rectángulo
base_label = Label(window, text="Base: ▄▄▄")
base_label.pack()
base_entry = Entry(window)
base_entry.pack()

# Etiqueta y cuadro de entrada para la altura del rectángulo, triángulo y trapecio
altura_label = Label(window, text="Altura: ▄▄▄  △   ▰")
altura_label.pack()
altura_entry = Entry(window)
altura_entry.pack()

# Etiqueta y cuadro de entrada para el lado del cuadrado y hexágono
lado_label = Label(window, text="Lado:  ▄  ⬟")
lado_label.pack()
lado_entry = Entry(window)
lado_entry.pack()

# Etiqueta y cuadro de entrada para la diagonal mayor del rombo
diagonal_mayor_label = Label(window, text="Diagonal mayor:  ◆")
diagonal_mayor_label.pack()
diagonal_mayor_entry = Entry(window)
diagonal_mayor_entry.pack()

# Etiqueta y cuadro de entrada para la diagonal menor del rombo
diagonal_menor_label = Label(window, text="Diagonal menor:  ◆")
diagonal_menor_label.pack()
diagonal_menor_entry = Entry(window)
diagonal_menor_entry.pack()

# Etiqueta y cuadro de entrada para la base mayor y menor del trapecio
base_mayor_label = Label(window, text="Base mayor:  ▰")
base_mayor_label.pack()
base_mayor_entry = Entry(window)
base_mayor_entry.pack()

# Etiqueta y cuadro de entrada para la base menor
base_menor_label = Label(window, text="Base menor:  ▰")
base_menor_label.pack()
base_menor_entry = Entry(window)
base_menor_entry.pack()

# Menú desplegable para seleccionar la figura
figura_menu = OptionMenu(window, figura_var, "Círculo", "Rectángulo", "Cuadrado", "Triángulo", "Rombo", "Trapecio", "Hexágono")
figura_menu.pack()

# Botón para calcular el área y perímetro
calcular_button = Button(window, text="Calcular", command=calcular_area_perimetro)
calcular_button.pack()

# Etiquetas para mostrar el resultado
area_label = Label(window, text="Área:")
area_label.pack()
perimetro_label = Label(window, text="Perímetro:")
perimetro_label.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
