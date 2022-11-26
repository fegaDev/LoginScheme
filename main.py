from tkinter import * 
from PIL import ImageTk 
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Sistema Login")
        self.root.geometry("1190x600 + 100 + 50")
        self.root.resizable(False,False)

    #Imagen de Fondo
        self.bg=ImageTk.PhotoImage(file="images/fondo.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0, y=0, relwidth=1,relheight=1)

    #Frame
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=330,y=150,width=50,height=400)
    #Titulo en el frame
    	title= Label(frame_login,text="Login here",font=("Impact",35,"bold"),fg="#6162FF",bg="white").place(x=90,y=30)
    	subtitle= Label(frame_login,text="Ingresar Plataforma",font=("Goudy old style",15,"bold",),fg="#1d1d1d",bg="white").place(x=90,y=100)

    #usuario
    	nameUser= Label(frame_login,text="Usuario",font=("Goudy old style",15,"bold"),fg="#grey",bg="white").place(x=90,y=150)
    	self.nameUser = Entry(frame_login,font=("Goudy old style",15),bg="#E7E6E6")
        self.nameUser.place(x=90,y=170,width=320,height=35)
    #password
    	namePassword= Label(frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="#grey",bg="white").place(x=90,y=150)
    	self.nameUser = Entry(frame_login,font=("Goudy old style",15),bg="#E7E6E6")
        self.nameUser.place(x=90,y=248,width=320,height=35)
    #Button
    	olvido = Button(frame_login,text="Olvide clave",font=("Goudy old style",15),bg=0,fg="#6162FF",bg="white").place(x=90,y=280))
    	ingresar = Button(frame_login,text="Ingresar",font=("Goudy old style",15),bg=0,fg="#6162FF",bg="white").place(x=90,y=320,width=180,height=40))


root = Tk()
obj = Login(root)
root.mainloop()


