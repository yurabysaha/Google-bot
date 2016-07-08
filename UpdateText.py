import os
import tkMessageBox
import Tkinter as tk
import platform

import xml.etree.ElementTree as ET

from tkinter import font


def xmlpath():
    if platform.system() == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()

class UpdateText:
    def __init__(self, body):
        self.text = tk.Text(body,
                         font="Verdana 12",
                         width=50, height=7)
        self.text.grid(row = 3, column = 2)

        title = tk.Label(body, text="Text", font="Arial 12")
        title.grid(row = 3, column = 1)
        butfont = font.Font(family='Ubuntu', size=10)
        but = tk.Button(body,
                     text="Update",
                     width=6, height=1,
                     bg="red", fg="white", font=butfont)
        but.bind("<Button-1>", self.updateText)
        but.grid(row=3, column=3)

    def updateText(self, event):
        doc = ET.parse(ROOT_PATH + 'text.xml')
        root = doc.getroot()
        text = doc.find('text')
        text.text = self.text.get(1.0, tk.END)

        doc.write(ROOT_PATH + 'text.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "New Text added"
        )