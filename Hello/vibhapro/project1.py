import os
from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk_
class Login:
    def __init__(self,root):
       self.root=root
       self.root.title("Login System")
       self.root.geometry("1199x600")

      # self.bg=PhotoImage(file="Camera Roll/HOLI.jpg")
       #self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

       Frame_login = Frame(self.root, bg="blue")
       Frame_login.place(x=330, y=150, width=850, height=600)

       title=Label(Frame_login, text="Admin Login ", font=("Impact",25, "bold"), fg="green", bg="white").place(x=300,y=50)
       subtitle=Label(Frame_login, text="For Color Detection Using Opencv", font=("Goudy old style",15, "bold"), fg="green", bg="white").place(x=250,y=100)

       lbl_user=Label(Frame_login, text="username", font=("Goudy old style",10, "bold"), fg="black", bg="white").place(x=280,y=140)
       self.username=Entry(Frame_login, font=("Goudy old style",15), bg="#E7E6E6")
       self.username.place(x=280,y=170, width=320, height=35)

       lbl_password=Label(Frame_login, text="password", font=("Goudy old style",10, "bold"), fg="black", bg="white").place(x=280,y=210)
       self.password=Entry(Frame_login, font=("Goudy old style",15), bg="#E7E6E6")
       self.password.place(x=280, y=240, width=320, height=35)

       forget=Button(Frame_login, text="forget password?",bd=0, cursor="hand2", font=("Goudy old style",12), fg="red", bg="white").place(x=280,y=280)
       submit=Button(Frame_login,command=self.check_function, cursor="hand2", text="Login",bd=0, font=("Goudy old style",15), bg="green", fg="white").place(x=300,y=350, width=180, height=40)

      # close=Button(Frame_login,command=self.check_function, cursor="hand2", text="close",bd=0, font=("Goudy old style",15), bg="grey", fg="white").place(x=90,y=320, width=180, height=40)

    def check_function(self):
        if self.username.get()=="" or self.password.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.username.get()!="admin" or self.password.get()!="admin123":
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
        else:
            messagebox.showinfo("welcome",f"Welcome {self.username.get()} For Detecting Color")
            os.system('opencv.py')

            #file=close('opencv.py')
            
            # messagebox.showinfo("welcome",f"Welcome {self.username.get()}")



root=Tk()
obj=Login(root)
root.mainloop()