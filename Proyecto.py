from tkinter import *

def send_data():
    nombres_info = nombres.get()
    apellidos_info = apellidos.get()
    profesion_info = profesion.get()
    edad_info = str(edad.get())
    cedula_info = str(cedula.get())

    print(nombres_info+"\t"+apellidos_info+"\t"+cedula_info+ "\t"+profesion_info+"\t"+edad_info)

#   Guardar información en un documento

    documento = open("registro.txt", "a")
    documento.write(nombres_info+"\t"+apellidos_info+"\t"+cedula_info+"\t"+profesion_info+"\t"+edad_info+"\n")
    documento.close()

    print("Usuario nuevo carnetizado. Nombres: {} | Apellidos: {} | C.I. {} ) ".format (nombres_info, apellidos_info, cedula_info))

    #Limpiar slots al terminar un registro
    nombres_entry.delete(0, END)
    apellidos_entry.delete(0, END)
    cedula_entry.delete(0, END)
    profesion_entry.delete(0, END)
    edad_entry.delete(0, END)

#Nueva instancia | Creación
mywindows= Tk()
mywindows.geometry("650x550")
mywindows.title("Formulario Carnetización")
mywindows.resizable(False, False)
mywindows.config(background="#125AC2")
main_title = Label(text="Carnetización | Arismendi/Guedez/Sieglett", font=("Open Sans", 13), bg = "#1F2E52", fg = "white", width = "500", height = "2")
    
#Definición de etiquetas para usuario

nombres_label = Label(text = "Nombres", bg = "#FFEEDD", font=("Open Sans", 11))
nombres_label.place(x = 22, y = 70)
apellidos_label = Label(text = "Apellidos", bg = "#FFEEDD", font=("Open Sans", 11))
apellidos_label.place(x = 22, y = 130)
profesion_label = Label(text = "Estudiante/Empleado", bg = "#FFEEDD", font=("Open Sans", 11))
profesion_label.place(x = 22, y = 190)
edad_label = Label(text = "Edad", bg = "#FFEEDD", font=("Open Sans", 11))
edad_label.place(x = 22, y = 250)
cedula_label = Label(text = "Cédula de Identidad", bg = "#FFEEDD", font=("Open Sans", 11))
cedula_label.place(x = 22, y = 310)

#Obtener datos de usuarios

nombres= StringVar()
apellidos= StringVar()
profesion= StringVar()
edad= StringVar()
cedula= StringVar()

nombres_entry= Entry(textvariable= nombres, width="40")
apellidos_entry= Entry(textvariable= apellidos, width="40")
profesion_entry= Entry(textvariable= profesion, width="40")
edad_entry= Entry(textvariable= edad, width="40")
cedula_entry= Entry(textvariable= cedula, width="40")

nombres_entry.place(x = 22, y = 100)
apellidos_entry.place(x= 22, y = 160)
profesion_entry.place(x= 22, y = 220)
edad_entry.place(x= 22, y = 280)
cedula_entry.place(x= 22, y = 340)

# Botón de guardado

btn_save= Button(mywindows, text ="Guardar información", font= ("Open Sans", 11), width= "20", height = "2", command= send_data, bg= "#00CD63")
btn_save.place(x = 22, y = 370)
main_title.pack()
mywindows.mainloop()

