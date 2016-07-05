import tkMessageBox
import Tkinter as tk

import xml.etree.ElementTree as ET


class UpdateText:
    def __init__(self, body):
        self.text = tk.Text(body,
                         font="Verdana 12",
                         width=50, height=7)
        self.text.grid(row = 3, column = 2)

        title = tk.Label(body, text="Text", font="Arial 12")
        title.grid(row = 3, column = 1)
        but = tk.Button(body,
                     text="Update",
                     width=6, height=1,
                     bg="red", fg="black")
        but.bind("<Button-1>", self.updateText)
        but.grid(row=3, column=3)

    def updateText(self, event):
        doc = ET.parse('text.xml')
        root = doc.getroot()
        text = doc.find('text')
        text.text = self.text.get(1.0, END)

        doc.write('text.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "New Text added"
        )