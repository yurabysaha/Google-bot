import tkMessageBox

from tkinter import *
import xml.etree.ElementTree as ET


class UserFields:
    def __init__(self, body, niz):
        title = Label(body, text="Facebook User", font="Arial 14")
        title.grid(row=0, column = 1, columnspan=2)

        title = Label(body, text="Current User", font="Arial 13")
        title.grid(row=1, column=1)

        doc = ET.parse('user.xml')
        mail = doc.find('email').text
        password = doc.find('password').text

        titleEmail = Label(body, text="Email : " + mail, font="Arial 12")
        titleEmail.grid(row=2, column=1, columnspan=2)

        titlePassword = Label(body, text="Password : " + password, font="Arial 12")
        titlePassword.grid(row=3, column=1, columnspan=2)

        title = Label(body, text="Change User", font="Arial 13")
        title.grid(row=4, column=1)
        self.email = Entry(body,
                         font="Verdana 12",
                          width=50)
        self.email.grid(row = 5, column = 2)

        title = Label(body, text="Login", font="Arial 12")
        title.grid(row = 5, column = 1)

        self.password = Entry(body,
                           font="Verdana 12",
                           width=50)

        self.password.grid(row=6, column=2)

        title = Label(body, text="Password", font="Arial 12")
        title.grid(row=6, column=1)

        but = Button(niz,
                          text="Update",
                          width=6, height=1,
                          bg="red", fg="black")

        but.bind("<Button-1>", self.updateUser)
        but.grid(row=1, column=3)


    def updateUser(self, titleEmail, event):
        doc = ET.parse('user.xml')

        emailf = doc.find('email')
        emailf.text = self.email.get()
        passwordf = doc.find('password')
        passwordf.text = self.password.get()

        doc.write('user.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "User Email&Password is updated"
        )


