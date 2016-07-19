import os
import tkMessageBox
import Tkinter as tk
import platform
import xml.etree.ElementTree as ET



def xmlpath():
    if platform.system() == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()

class GroupLinkField:
    def __init__(self, body):
        self.glink = tk.Text(body,
                         font="Verdana 12",
                         width=50, height=10)
        self.glink.grid(row = 2, column = 2)

        title = tk.Label(body, text="Group Link", font="Arial 12")
        title.grid(row = 2, column = 1)
        #butfont = font.Font(family='Ubuntu', size=10)
        but = tk.Button(body,
                     text="Update",
                     width=6, height=1,
                     bg="red", fg="white")
        but.bind("<Button-1>", self.updateGroup)
        but.grid(row=2, column=3)

    def updateGroup(self, event):
        doc = ET.parse(ROOT_PATH + 'groupLink.xml')
        root = doc.getroot()
        deleted = doc.findall('glink')
        for item in deleted:
          root.remove(item)

        newLink = self.glink.get(1.0, tk.END)
        pp = newLink.split()
        for item in pp:
            new = ET.Element('glink')
            new.text = item
            root.append(new)

        doc.write(ROOT_PATH + 'groupLink.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "Groups link is updated"
        )