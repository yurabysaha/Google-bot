import tkMessageBox
import Tkinter as tk


import xml.etree.ElementTree as ET


class GroupLinkField:
    def __init__(self, body):
        self.glink = tk.Text(body,
                         font="Verdana 12",
                         width=50, height=10)
        self.glink.grid(row = 2, column = 2)

        title = tk.Label(body, text="Group Link", font="Arial 12")
        title.grid(row = 2, column = 1)
        but = tk.Button(body,
                     text="Update",
                     width=6, height=1,
                     bg="red", fg="black")
        but.bind("<Button-1>", self.updateGroup)
        but.grid(row=2, column=3)

    def updateGroup(self, event):
        doc = ET.parse('groupLink.xml')
        root = doc.getroot()
        deleted = doc.findall('glink')
        for item in deleted:
          root.remove(item)

        newLink = self.glink.get(1.0, END)
        pp = newLink.split()
        for item in pp:
            new = ET.Element('glink')
            new.text = item
            root.append(new)

        doc.write('groupLink.xml', encoding="utf-8", xml_declaration=True)
        tkMessageBox.showinfo(
            "Updated",
            "Groups link is updated"
        )