import SettingsBody
from BaseTest import *
from UpdatePictureLink import *
import BaseTest
from UpdateGroupLink import *
from UpdateText import UpdateText
import Tkinter as tk
import platform
from tkinter import font

root = tk.Tk()
root.title('Google-bot')
root.resizable(width=False, height=False)
root.minsize(width=500, height=400)


def xmlpath():
    if platform.system() == "Linux":
        return '/'
    else:
        return '\\'

ROOT_PATH=os.getcwd() + xmlpath()


class But_start:
    def __init__(self):
        butfont = font.Font(family='Ubuntu', size=12)
        self.but = tk.Button(niz,
                            text="Start Bot",
                            width=12, height=3,
                            bg="green", fg="white", font=butfont)
        self.but.bind("<Button-1>", self.startBot)
        self.but.pack()

    def startBot(self, event):
        BaseTest.unittest.TextTestRunner().run(suite())
        Statistic()


menu = tk.Frame(root, width=700, height=27, bg="darkred")
body = tk.Frame(root, width=500, height=200)
niz = tk.Frame(root, width=500, height=150, bg="darkblue")
Settingsbody = tk.Frame(root, width=500, height=200)
Settingsniz = tk.Frame(root, width=500, height=150)
statisticBody =  tk.Frame(root, width=500, height=200)
statisticNiz = tk.Frame(root, width=500, height=150)
menu.grid(row=1, sticky='W')


body.grid(row=2)
niz.grid(row=3)


class Settings:
    def __init__(self, place):
        butfont = font.Font(family='Ubuntu', size=10)
        self.but = tk.Button(place,
                              text="Settings",
                              width=8, height=1,
                              bg="green", fg="white", font=butfont)

        self.but.bind("<Button-1>", self.openSettings)
        self.but.grid(row=1, column=2)

    def openSettings(self, event):
        SettingsBody.UserFields(Settingsbody, Settingsniz)
        body.grid_forget()
        niz.grid_forget()
        Settingsbody.grid(row=2)
        Settingsniz.grid(row=3)


class mainWindowBtn:
    def __init__(self, place):
        butfont = font.Font(family='Ubuntu', size=10)
        self.but = tk.Button(place,
                          text="Main",
                          width=8, height=1,
                          bg="green", fg="white", font=butfont)

        self.but.bind("<Button-1>", self.mWindow)
        self.but.grid(row=1, column=1)

    def mWindow(self, event):
        Settingsbody.grid_forget()
        Settingsniz.grid_forget()
        body.grid(row=2)
        niz.grid(row=3)


class mWindow:
    def __init__(self):
        mainWindowBtn(menu)
        Settings(menu)
        UpdateLink(body)
        GroupLinkField(body)
        UpdateText(body)
        But_start()


class Statistic:
    def __init__(self):
        body.grid_forget()
        niz.grid_forget()
        statisticBody.grid(row=2)
        statisticNiz.grid(row=3)

        appHighlightFont = font.Font(family='Helvetica', size=12, weight='bold')
        file = open(ROOT_PATH + 'Statistic.txt', 'r')
        notPostedL = tk.Label(statisticBody, text= file.read() + " groups", font=appHighlightFont)
        notPostedL.grid(row=1, column=2, columnspan=2)
        but = tk.Button(statisticNiz,
                            text="Repeat",
                            width=8, height=3,
                            bg="green", fg="black")
        but.bind("<Button-1>", self.repeat)
        but.grid(row=1, column=2, columnspan=2)


    def repeat(self, event):
        print "Hi"




mWindow()


root.mainloop()