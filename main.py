import tkinter

def saludar():
    print("Holii")
def saludarA(toSaludar):
    print(f'Hola {toSaludar}')

if __name__ == "__main__":
    print('Hagamos esto una vez más!')
    ventana = tkinter.Tk()
    ventana.geometry("400x300")

    #Titulos titulos
    etiqueta = tkinter.Label(ventana, text = "Hello World", bg = "red")
    # etiqueta.pack(fill = tkinter.Y, expand=True)
    etiqueta.pack(fill = tkinter.BOTH, expand=True)

    #Boton con funcion sin parametros
    bonton1 = tkinter.Button(
        ventana,
        text= "Presiona",
        command=saludar,
        padx = 40, 
        pady=10)
    bonton1.pack()
    #Boton con funcion con parametros
    bonton2 = tkinter.Button(
        ventana,
        text= "Presioname",
        command= lambda: saludarA('Amigo'),
        padx = 40, 
        pady=10)
    bonton2.pack()

    ##Widgets

    #Entrada de texto
    cajaTexto = tkinter.Entry(ventana, font = "Helvetica 30")
    cajaTexto.pack()

    #Boton para obtener texto
    bonton3 = tkinter.Button(
        ventana,
        text= "Get Text",
        command= lambda: saludarA('Amigo'),
        padx = 40, 
        pady=10)
    bonton3.pack()

    ventana.mainloop()
