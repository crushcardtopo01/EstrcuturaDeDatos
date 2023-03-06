import tkinter as tk
from tkinter import ttk
class Aplicacion(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.etiqueta_temp_celsius = ttk.Label(
            parent, text="Temperatura en ºC:")
        self.etiqueta_temp_celsius.place(x=20, y=20)
        self.caja_temp_celsius = ttk.Entry(parent)
        self.caja_temp_celsius.place(x=140, y=20, width=60)
        self.boton_convertir = ttk.Button(
            parent, text="Convertir", command=self.convertir_temp)
        self.boton_convertir.place(x=20, y=60)
        self.etiqueta_temp_kelvin = ttk.Label(
            parent, text="Temperatura en K: n/a")
        self.etiqueta_temp_kelvin.place(x=20, y=120)
        self.etiqueta_temp_fahrenheit = ttk.Label(
            parent, text="Temperatura en ºF: n/a")
        self.etiqueta_temp_fahrenheit.place(x=20, y=160)
    def convertir_temp(self):
        temp_celsius = float(self.caja_temp_celsius.get())
        temp_kelvin = temp_celsius + 273.15
        temp_fahrenheit = temp_celsius*1.8 + 32
        self.etiqueta_temp_kelvin.config(
            text=f"Temperatura en K: {temp_kelvin}")
        self.etiqueta_temp_fahrenheit.config(
            text=f"Temperatura en ºF: {temp_fahrenheit}")
ventana = tk.Tk()
ventana.title("Conversor de temperatura")
ventana.config(width=400, height=300)
app = Aplicacion(ventana)
ventana.mainloop()