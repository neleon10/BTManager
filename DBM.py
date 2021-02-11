from tkinter import *
from tkinter import messagebox  
import sqlite3  

#Ventana principal
root=Tk()
root.title("Data Base Creator")

#-----------------DB functions --------------------
def infoExit():
	exitsalir=messagebox.askyesno("Atención","¿Desea salir del programa?")
	if exitsalir==True:
		root.destroy()

def connectDB():
			newDB=sqlite3.connect("Alumnos")
			myCursor=newDB.cursor()
			try:
				myCursor.execute('''
					CREATE TABLE ALUMNOS_GUADALUPE (
					ID INTEGER PRIMARY KEY AUTOINCREMENT,
					NOMBRE_ALUMNO VARCHAR (50),
					APELLIDO_ALUMNO VARCHAR (50),
					PASSWORD VARCHAR (20),
					DIRECCION VARCHAR (50),
					COMENTARIOS VARCHAR (1000))
				''')
				messagebox.showinfo("Aviso","Su base de datos se creo con éxito")
				
			except:
				messagebox.showwarning("Atención","Su base de datos ya ha sido creada")


#---------------------------CRUD---------------------------
def create():
	newDB=sqlite3.connect("Alumnos")
	myCursor=newDB.cursor()
	datos=nombreEntryVariable.get(),apellidoEntryVariable.get(),passwordEntryVariable.get(),direccionEntryvariable.get(),cuadroText.get(1.0,END)
	myCursor.execute("INSERT INTO ALUMNOS_GUADALUPE VALUES (NULL,?,?,?,?,?)",(datos))

   
    #ATENCION ES UNA FORMA DIFERENTE DE HACERLO-------------
    
	"""myCursor.execute("INSERT INTO ALUMNOS_GUADALUPE \
	VALUES(NULL,'" + nombreEntryVariable.get() + 
	"','" + apellidoEntryVariable.get()+ 
	"','" + passwordEntryVariable.get()+
	"','"+direccionEntryvariable.get()+
	"','"+cuadroText.get(1.0,END)+"')")"""

	newDB.commit()
	messagebox.showinfo("Aviso","Su registro ha sido agregado satisfactoriamente")
	newDB.close()

def read():
	
	newDB=sqlite3.connect("Alumnos")
	myCursor=newDB.cursor()
	myCursor.execute("SELECT * FROM ALUMNOS_GUADALUPE WHERE ID=" + iDnumberEntry.get())
	alumno=myCursor.fetchall()#alumno en este caso es un array
	for i in alumno:
		iDnumberEntry.set(i[0])
		nombreEntryVariable.set(i[1])
		apellidoEntryVariable.set(i[2])
		passwordEntryVariable.set(i[3])
		direccionEntryvariable.set(i[4])
		cuadroText.insert(1.0,i[5])
		
	newDB.commit()
	newDB.close()

def updaTe():
	newDB=sqlite3.connect("Alumnos")
	myCursor=newDB.cursor()
	datos=nombreEntryVariable.get(),apellidoEntryVariable.get(),passwordEntryVariable.get(),direccionEntryvariable.get(),cuadroText.get(1.0,END)
	myCursor.execute("UPDATE ALUMNOS_GUADALUPE SET NOMBRE_ALUMNO=?,APELLIDO_ALUMNO=?,PASSWORD=?,DIRECCION=?,COMENTARIOS=?" +
		"WHERE ID=" + iDnumberEntry.get(),(datos))

	#ATENCION ES UNA FORMA DIFERENTE DE HACERLO-------------

	"""myCursor.execute("UPDATE ALUMNOS_GUADALUPE SET NOMBRE_ALUMNO='"+nombreEntryVariable.get()+
		"',APELLIDO_ALUMNO='"+apellidoEntryVariable.get()+
		"',PASSWORD='"+passwordEntryVariable.get()+
		"',DIRECCION='"+direccionEntryvariable.get()+
		"',COMENTARIOS='"+cuadroText.get(1.0,END)+
		"' WHERE ID=" + iDnumberEntry.get())"""

	newDB.commit()
	messagebox.showinfo("Aviso","Su registro ha sido actualizado")
	newDB.close()

def deleteField():

	delete=messagebox.askyesno("Atención","¿Desea eliminar el alumno de la base de datos?")
	if delete==True:
		newDB=sqlite3.connect("Alumnos")
		myCursor=newDB.cursor()
		myCursor.execute ("DELETE FROM ALUMNOS_GUADALUPE WHERE ID=" + iDnumberEntry.get())
		newDB.commit()
		newDB.close()
		messagebox.showinfo("Aviso","El alumno ha sido eliminado de la base de datos")
		deleteFields()
	else:
		messagebox.showinfo("Aviso","El alumno no ha sido borrado")


#-----------------------BORRAR Function--------------------------
def deleteFields():
	iDnumberEntry.set("")
	nombreEntryVariable.set("")
	apellidoEntryVariable.set("")
	passwordEntryVariable.set("")
	direccionEntryvariable.set("")
	cuadroText.delete(1.0,END)


#---barra menu-----
barraMenu=Menu(root)
root.config(menu=barraMenu)

#--------opcion DB botones---------
DB_Menu=Menu(barraMenu,tearoff=0)
DB_Menu.add_command(label="Connect",command=connectDB)
DB_Menu.add_command(label="Exit",command=infoExit)
barraMenu.add_cascade(label="DB", menu=DB_Menu)  

#--------Opcion borrar campos--------
borrar_campos=Menu(barraMenu,tearoff=0)
borrar_campos.add_command(label="Borrar campos",command=deleteFields)
barraMenu.add_cascade(label="Borrar", menu=borrar_campos)

#----------Menu CRUD--------------
crud_Menu=Menu(barraMenu,tearoff=0)
crud_Menu.add_command(label="Create",command=create)
crud_Menu.add_command(label="Read",command=read)
crud_Menu.add_command(label="Update",command=updaTe)
crud_Menu.add_command(label="Delete",command=deleteField)
barraMenu.add_cascade(label="CRUD",menu=crud_Menu)

#-----------Menu Ayuda------------
help_Menu=Menu(barraMenu,tearoff=0)
help_Menu.add_command(label="Licence")
help_Menu.add_command(label="About us...")
barraMenu.add_cascade(label="Help",menu=help_Menu)

#----------FRAME --LABELS and entries----------------

mainFrame=Frame(root,width=300,height=400).pack()

iDnumberEntry=StringVar()
iDlabel=Label(mainFrame,text="ID").place(x=5,y=5)
iDEntry=Entry(mainFrame,textvariable=iDnumberEntry).place(x=75,y=5)

nombreEntryVariable=StringVar()
nombreLabel=Label(mainFrame,text="Nombre: ").place(x=5,y=30)
nombreEntry=Entry(mainFrame,textvariable=nombreEntryVariable).place(x=75,y=30)

apellidoEntryVariable=StringVar()
apellidoLabel=Label(mainFrame,text="Apellido: ").place(x=5,y=55)
apellidoEntry=Entry(mainFrame,textvariable=apellidoEntryVariable).place(x=75,y=55)

passwordEntryVariable=StringVar()
passwordLabel=Label(mainFrame,text="Password: ").place(x=5,y=80)
passwordEntry=Entry(mainFrame,show="*",textvariable=passwordEntryVariable).place(x=75,y=80)

direccionEntryvariable=StringVar()
direccionLabel=Label(mainFrame,text="Dirección: ").place(x=5,y=105)
direccionEntry=Entry(mainFrame,textvariable=direccionEntryvariable).place(x=75,y=105)

cuadroLabel=Label(mainFrame,text="Comentarios: ").place(x=5,y=150)
#--------------------SCROLLBAR and TEXT---------------


frame1=Frame(mainFrame)
frame1.place(x=5,y=170)
scrol=Scrollbar(frame1)
scrol.pack(side=RIGHT,fill=Y)
cuadroText=Text(frame1,width=32,height=10,wrap=WORD,yscrollcommand=scrol.set)
cuadroText.pack()
scrol.config(command=cuadroText.yview)


#-----------------BOTONES INFERIORES------------------
buttonFrame=Frame(mainFrame).pack()

buttonCreate=Button(buttonFrame,text="Create",command=create).place(x=10,y=350)
buttonRead=Button(buttonFrame,text="Read",command=read).place(x=75,y=350)
buttonUpdate=Button(buttonFrame,text="Update",command=updaTe).place(x=135,y=350)
buttonDelete=Button(buttonFrame,text="Delete",command=deleteField).place(x=205,y=350)

#-------------------THE END--------------------------
root.mainloop()