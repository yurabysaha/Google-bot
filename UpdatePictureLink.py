import os
import tkMessageBox
import tkSimpleDialog
import Tkinter as tk
from tkFileDialog import askopenfilename
import platform
import xml.etree.ElementTree as ET

def xmlpath():
    if platform.system() == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()


def open_file_handler():
    filePath = askopenfilename()

    doc = ET.parse(ROOT_PATH + 'pictureLink.xml')
    root = doc.getroot()
    django = doc.find('link')
    django.text = filePath
    doc.write(ROOT_PATH + 'pictureLink.xml', encoding="utf-8", xml_declaration=True)

    tkMessageBox.showinfo(
    "Updated",
    "Picture is updated"
)


class UpdateLink:
    def __init__(self, body):
        self.but = tk.Button(body, command=open_file_handler, padx=100, text="Select Picture")
        self.but.grid(row = 1, column = 2)

        title = tk.Label(body, text="Picture link", font="Arial 12")
        title.grid(row = 1, column = 1)



