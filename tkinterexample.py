import tkinter as tk


# Función que se ejecuta al presionar el botón
def saludar():
    print("¡Hola desde el botón de Tkinter!")
    etiqueta.config(text="¡Botón presionado con éxito!")


# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Mi App de Taquilla")
ventana.geometry("300x250")

# Creamos una etiqueta de texto
etiqueta = tk.Label(ventana, text="Bienvenido a la app", font=("Arial", 12))
etiqueta.pack(pady=20)

# Creamos el botón interactivo
boton = tk.Button(
    ventana,
    text="Hacer clic",
    command=saludar,
    bg="blue",
    fg="white",
    font=("Arial", 10),
)
boton.pack(pady=10)

# Mantenemos la ventana abierta en pantalla
ventana.mainloop()
