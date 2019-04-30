from tkinter import *

def Calcular():
    c = int(campo.get())
    cc = int(campoo.get())
    result= c+cc

    resultado["text"] = str(result)


 
 



instancia= Tk()

instancia.title("Calculadora")

instancia.geometry = ("500X400")

label = Label(instancia, text = "valor1 ")
label.pack()

campo = Entry(instancia)
campo.pack()

bt = Button(instancia,text='aperte', command = Calcular)
bt.pack()

labell = Label(instancia, text ="valor2")
labell.pack()

campoo = Entry(instancia)
campoo.pack()

btt = Button(instancia, text = 'aperte2', command = Calcular )

btt.pack()

resultado = Label(instancia, text ='')
resultado.pack()

instancia.mainloop()
