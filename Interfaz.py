import tkinter as tk

def textoconsole():
    codigo = cajacodigo.get("1.0",'end-1c') #obtengo el texto que el usuario ingresa cuando da click en check
    print(codigo) #muestra en consola el texto del user
    with open("codigo.txt", "w") as archivo:
        archivo.write(codigo) #lo guardo en un txt

ventana = tk.Tk()
ventana.geometry("730x700")

cajacodigo = tk.Text(ventana, width = 30,height=30 )
cajaconsole = tk.Text(ventana, width = 30,height=30 )
cajafiles = tk.Text(ventana, width = 30,height=30 )

titulo = tk.Label(ventana, text="RUBYLIX\n Simple Ruby Syntax Checker")
btopenfile = tk.Button(ventana, text = "Open file", width = 10, height=2)
btcheck = tk.Button(ventana, text = "Check", width = 10, height=2, command=textoconsole)

titulo.grid(row = 0, column = 1, pady=10)
btopenfile.grid(row = 0, column = 0, pady=10)
btcheck.grid(row = 0, column = 2, pady=10,)

cajacodigo.grid(row=1,column=1, pady=10)
cajaconsole.grid(row=1,column=2, pady=10)
cajafiles.grid(row=1,column=0, pady=10)


ventana.mainloop()

