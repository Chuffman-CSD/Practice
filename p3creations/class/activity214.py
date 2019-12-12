#!/usr/bin/python3
#Chris Huffman
#11-21-19

import tkinter as tk

default = ('Times New Roman', 15)

#class goes here
class Login(tk.Frame):
    #global variables
    login_attempts = 0

    def __init__(self):
        tk.Frame.__init__(self)

        #username aspects
        self.lbl_username = tk.Label(self,text="Username: ",font = default)
        self.lbl_username.grid(row = 0, column = 0)

        self.ent_username = tk.Entry(self,bg="white",font = default)
        self.ent_username.grid(row=0,column=1)

        #password aspects
        self.lbl_password = tk.Label(self,text="Password: ",font = default)
        self.lbl_password.grid(row = 1, column = 0)

        self.ent_password = tk.Entry(self,show="*",bg="white",font = default)
        self.ent_password.grid(row = 1, column = 1)

        self.btn_login = tk.Button(self,text="Login",bg="green",command=self.raise_authenticate,font = default)
        
        self.lbl_instruction1 = tk.Label(self,text = "To login,",font = default)
        self.lbl_instruction1.grid(row = 2, column = 0, columnspan = 2)

        self.lbl_instruction2 = tk.Label(self,text = "fill out the boxes and click login.",font = default)
        self.lbl_instruction2.grid(row = 3, column = 0, columnspan = 2)

        #btn_login.pack(pady=5)
        self.btn_login.grid(row = 4, column = 0, columnspan = 2)

        # - - - frame authentication - - -
        self.frame_authentication = tk.Frame(root)
        self.frame_authentication.grid(row = 0, column = 0, sticky = "news")

        self.tkraise()
        self.btn_cancel = tk.Button(self.frame_authentication,text="Cancel",bg="Yellow",command=self.raise_cancel)
        self.btn_cancel.pack(pady=5)
        
    
    def raise_authenticate(self):
        if self.ent_username.get() == "admin" and self.ent_password.get() == "secret":
            Login.login_attempts = 0
            self.ent_username.configure(bg = "green")
            self.ent_password.configure(bg = "green")
            self.frame_authentication.tkraise()
        else:
            global login_attempts
            if Login.login_attempts >= 3:
                self.btn_login.configure(state = "disabled",bg = "grey")
            Login.login_attempts += 1
            self.ent_username.configure(bg = "red")
            self.ent_password.configure(bg = "red")
    def raise_cancel(self):
        self.tkraise()

'''program to experiment with tkinter, buttons and widgets'''

root = tk.Tk()


frame = tk.Frame()


#creates a title
root.title("Activity 2.1.4")

#creates a shape for the window
root.geometry()

#Create login frame
frame_login = Login()
frame_login.grid(row = 0, column = 0, sticky = "news")

root.mainloop()


