import tkinter as tk
from tkinter import simpledialog
from math import sqrt

def calcular_manhattan():
    try:
        x1 = int(simpledialog.askstring("Manhattan", "Ingresa x del punto 1:"))
        y1 = int(simpledialog.askstring("Manhattan", "Ingresa y del punto 1:"))
        x2 = int(simpledialog.askstring("Manhattan", "Ingresa x del punto 2:"))
        y2 = int(simpledialog.askstring("Manhattan", "Ingresa y del punto 2:"))
        manhattan = abs(x2 - x1) + abs(y2 - y1)
        pantalla.set(f"Manhattan: {manhattan}")
    except (TypeError, ValueError):
        pantalla.set("Error en entrada")

def calcular_euclidiana():
    try:
        x1 = int(simpledialog.askstring("Euclidiana", "Ingresa x del punto 1:"))
        y1 = int(simpledialog.askstring("Euclidiana", "Ingresa y del punto 1:"))
        x2 = int(simpledialog.askstring("Euclidiana", "Ingresa x del punto 2:"))
        y2 = int(simpledialog.askstring("Euclidiana", "Ingresa y del punto 2:"))
        euclidiana = sqrt((x2 - x1)**2 + (y2 - y1)**2)
        pantalla.set(f"Euclidiana: {euclidiana:.2f}")
    except (TypeError, ValueError):
        pantalla.set("Error en entrada")

def click(boton):
    actual = pantalla.get()
    if boton == "C":
        pantalla.set("0")
    elif boton == "=":
        try:
            pantalla.set(str(eval(actual)))
        except:
            pantalla.set("Error")
    elif boton == "M":
        calcular_manhattan()
    elif boton == "E":
        calcular_euclidiana()
    else:
        pantalla.set(actual + boton if actual != "0" else boton)

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")
ventana.configure(bg="#FFFFFF")
pantalla = tk.StringVar(value="0")

tk.Label(ventana, textvariable=pantalla, bg="#111", fg="#fff",
         font=("Arial", 20, "bold"), height=2).pack(fill="x", padx=10, pady=10)

botones = [
    ["C", "M", "E", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "00", ".", "="],
]

for fila in botones:
    contenedor = tk.Frame(ventana, bg="#000")
    contenedor.pack(fill="x", padx=10, pady=2)
    for boton in fila:
        color_fondo = (
            "#1B1A63" if boton in "+-*/=C" else
            "#3498db" if boton in ("M", "E") else
            "#34495e"
        )
        boton_widget = tk.Label(
            contenedor, text=boton, font=("Arial", 14, "bold"),
            bg=color_fondo, fg="white", width=5, height=2, relief="flat"
        )
        boton_widget.bind("<Button-1>", lambda e, b=boton: click(b))
        boton_widget.pack(side="left", padx=2)

ventana.mainloop()
