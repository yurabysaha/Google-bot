import os
import tkMessageBox
import Tkinter as tk


import xml.etree.ElementTree as ET
def xmlpath():
    if os.uname()[0] == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()

class UserFields:
    def __init__(self, body, niz):
        title = tk.Label(body, text="Facebook User", font="Arial 14")
        title.grid(row=0, column = 1, columnspan=2)

        title = tk.Label(body, text="Current User", font="Arial 13")
        title.grid(row=1, column=1)

        doc = ET.parse(ROOT_PATH + 'user.xml')
        mail = doc.find('email').text
        password = doc.find('password').text

        titleEmail = tk.Label(body, text="Email : " + mail, font="Arial 12")
        titleEmail.grid(row=2, column=1, columnspan=2)

        titlePassword = tk.Label(body, text="Password : " + password, font="Arial 12")
        titlePassword.grid(row=3, column=1, columnspan=2)

        title = tk.Label(body, text="Change User", font="Arial 13")
        title.grid(row=4, column=1)
        self.email = tk.Entry(body,
                         font="Verdana 12",
                          width=50)
        self.email.grid(row = 5, column = 2)

        title = tk.Label(body, text="Login", font="Arial 12")
        title.grid(row = 5, column = 1)

        self.password = tk.Entry(body,
                           font="Verdana 12",
                           width=50)

        self.password.grid(row=6, column=2)

        title = tk.Label(body, text="Password", font="Arial 12")
        title.grid(row=6, column=1)

        but = tk.Button(niz,
                          text="Update",
                          width=6, height=1,
                          bg="red", fg="black")

        but.bind("<Button-1>", self.updateUser)
        but.grid(row=1, column=3)


    def updateUser(self, event):
        doc = ET.parse(ROOT_PATH + 'user.xml')

        emailf = doc.find('email')
        emailf.text = self.email.get()
        passwordf = doc.find('password')
        passwordf.text = self.password.get()

        doc.write(ROOT_PATH + 'user.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "User Email&Password is updated"
        )

