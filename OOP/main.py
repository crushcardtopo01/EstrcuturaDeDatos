from Dog import Dog
from stack import *
import tkinter as tk
from tkinter import ttk

class VentanaNombre(tk.Toplevel):
    def __init__(self, *args, callback=None, **kwargs):
        super().__init__(*args, **kwargs)
        # callback es una función que esta ventana llamará
        # una vez presionado el botón para comunicarle el nombre
        # ingresado a la ventana padre.
        self.callback = callback
        self.config(width=300, height=90)
        # Deshabilitar el botón para maximizar la ventana.
        self.resizable(0, 0)
        self.title("Ingresa tu nombre")
        self.caja_nombre = ttk.Entry(self)
        self.caja_nombre.place(x=20, y=20, width=260)
        self.boton_listo = ttk.Button(
            self,
            text="¡Listo!",
            command=self.boton_listo_presionado
        )
        self.boton_listo.place(x=20, y=50, width=260)
        self.focus()
        self.grab_set()
    
    def boton_listo_presionado(self):
        # Obtener el dato ingresado y llamar a la función
        # especificada al crear esta ventana.
        self.callback(self.caja_nombre.get())
        # Cerrar la ventana.
        self.destroy()

def boton_listo_presionado(self):
        # Obtener el dato ingresado y llamar a la función
        # especificada al crear esta ventana.
        self.callback(self.caja_nombre.get())
        # Cerrar la ventana.
        self.destroy()

        
class my_stack(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)

        self.main_label = ttk.Label(
            parent, text="Stack with Dogs 🐈")
        self.main_label.place(x=140, y=0)

        self.add_dog = ttk.Button(
            parent, text="Add dog", command=self.add_dog)
        self.add_dog.place(x=150, y=30)

        self.remove_dog = ttk.Button(
            parent, text="remove dog")
        self.remove_dog.place(x=150, y=60)

        self.show_dogs = ttk.Button(
            parent, text="show dogs")
        self.show_dogs.place(x=150, y=90)

    def add_dog(self):
        self.ventana_nombre = VentanaNombre(
            callback=""
        )

        # ventana_secundaria = tk.Toplevel()
        # ventana_secundaria.title("Add Dog")
        # ventana_secundaria.config(width=300, height=200)
        # self.caja_nombre = ttk.Entry(self)
        # self.caja_nombre.place(x=20, y=20, width=260)
        # # Crear un botón dentro de la ventana secundaria
        # # para cerrar la misma.
        # boton_cerrar = ttk.Button(
        #     ventana_secundaria,
        #     text="Cerrar ventana", 
        #     command=ventana_secundaria.destroy
        # )
        # boton_cerrar.place(x=75, y=75)
        # ventana_secundaria.focus()
        # ventana_secundaria.grab_set()
        


ventana = tk.Tk()
ventana.title("Stack")
ventana.config(width=400, height=300)
app = my_stack(ventana)
ventana.mainloop()