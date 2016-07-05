import lala as lala

import SettingsBody
from BaseTest import *
from UpdatePictureLink import *
import BaseTest
from UpdateGroupLink import *
from UpdateText import UpdateText

root = Tk()
root.title('Botter')


class But_start:
    def __init__(self):
        self.but = Button(niz,
                            text="Start Bot",
                            width=10, height=3,
                            bg="green", fg="black")
        self.but.bind("<Button-1>", self.startBot)
        self.but.pack()

    def startBot(self, event):

        BaseTest.unittest.TextTestRunner().run(suite())



menu = Frame(root, width=700, height=27, bg="darkred")
body = Frame(root, width=500, height=200)
niz = Frame(root, width=500, height=150, bg="darkblue")
Settingsbody = Frame(root, width=500, height=200)
Settingsniz = Frame(root, width=500, height=150)
statisticBody =  Frame(root, width=500, height=200)
statisticNiz = Frame(root, width=500, height=150)
menu.grid(row=1, sticky=W)
body.grid(row=2)
niz.grid(row=3)



class Settings:
    def __init__(self, place):
        self.but = Button(place,
                              text="Settings",
                              width=8, height=1,
                              bg="green", fg="black")

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
        self.but = Button(place,
                          text="Main",
                          width=8, height=1,
                          bg="green", fg="black")

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
        notPostedL = Label(statisticBody, text="Not Posted in : " + " groups", font="Arial 12")
        notPostedL.grid(row=1, column=1, columnspan=2)
        statisticBody.grid(row=2)
        statisticNiz.grid(row=3)





mWindow()


root.mainloop()