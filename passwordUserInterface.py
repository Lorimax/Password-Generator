from tkinter import *
from passwordEventHandler import *
from passwordEvent import *
from passwordSettings import *
from passwordSettings2EventConverter import *

class GUI():
    __window = Tk()
    __eventHandler = PasswordEventHandler()
    __passwordSettings = []
    __settings2Event = PasswordSettings2EventConverter()
    __upperCaseButton = Button(None, text='Upper case characters')
    __lowerCaseButton = Button(None, text='Lower case characters')
    __numberButton = Button(None, text='Numbers')
    __specialCharacterButton = Button(None, text='Special characters')
    __readableNoNumberButton = Button(None, text='Readable without numbers')
    __readableNumberButton = Button(None, text='Readable with numbers')
    __createPasswordButton = Button(None, text='Create Password')
    __clearButton = Button(None, text='Clear')



    def __invokeEventHandler(self, event):
        if not self.__passwordSettings:
            self.output.insert(INSERT, "Nothing selected!\n")
            self.output.pack()
        else:
            converter = PasswordSettings2EventConverter()
            self.__eventHandler.executeEvent(converter.convertSettings2Event(self.__passwordSettings), self.output)

    def __setUpperCase(self, event):
        self.__drawSetting(PasswordSettings.UPPER_CASE)
        self.__passwordSettings.append(PasswordSettings.UPPER_CASE)

    def __setLowerCase(self, event):
        self.__drawSetting(PasswordSettings.LOWER_CASE)
        self.__passwordSettings.append(PasswordSettings.LOWER_CASE)

    def __setNumber(self, event):
        self.__drawSetting(PasswordSettings.NUMBER)
        self.__passwordSettings.append(PasswordSettings.NUMBER)

    def __setSpecialCharacter(self, event):
        self.__drawSetting(PasswordSettings.SPECIAL_CHARACTER)
        self.__passwordSettings.append(PasswordSettings.SPECIAL_CHARACTER)

    def __setReadableNoNumber(self, event):
        self.__clear('<Button-1>')
        self.__drawSetting(PasswordSettings.READABLE_NO_NUMBER)
        self.__passwordSettings.append(PasswordSettings.READABLE_NO_NUMBER)

    def __setReadableNumber(self, event):
        self.__clear('<Button-1>')
        self.__drawSetting(PasswordSettings.READABLE_NUMBER)
        self.__passwordSettings.append(PasswordSettings.READABLE_NUMBER)


    def __clear(self, event):
        self.__passwordSettings.clear()
        self.output.delete('1.0', END)


    def __drawSetting(self,setting):
        if setting == PasswordSettings.UPPER_CASE:
            self.output.insert(INSERT, "Upper case characters selected\n")
            self.output.pack()
        elif setting == PasswordSettings.LOWER_CASE:
            self.output.insert(INSERT, "Lower case characters selected\n")
            self.output.pack()
        elif setting == PasswordSettings.NUMBER:
            self.output.insert(INSERT, "Numbers selected\n")
            self.output.pack()
        elif setting == PasswordSettings.SPECIAL_CHARACTER:
            self.output.insert(INSERT, "Special characters selected\n")
            self.output.pack()
        elif setting == PasswordSettings.READABLE_NO_NUMBER:
            self.output.insert(INSERT, "Readable without numbers selected\n")
            self.output.pack()
        elif setting == PasswordSettings.READABLE_NUMBER:
            self.output.insert(INSERT, "Readable with numbers selected\n")
            self.output.pack()



    def __bindButtons(self):
        self.__upperCaseButton.bind('<Button-1>', self.__setUpperCase)
        self.__lowerCaseButton.bind('<Button-1>', self.__setLowerCase)
        self.__numberButton.bind('<Button-1>', self.__setNumber)
        self.__specialCharacterButton.bind('<Button-1>', self.__setSpecialCharacter)
        self.__createPasswordButton.bind('<Button-1>', self.__invokeEventHandler)
        self.__readableNoNumberButton.bind('<Button-1>', self.__setReadableNoNumber)
        self.__readableNumberButton.bind('<Button-1>', self.__setReadableNumber)
        self.__clearButton.bind('<Button-1>', self.__clear)


    def draw(self):
        self.output = Text(self.__window)
        self.__bindButtons()
        self.__upperCaseButton.pack()
        self.__lowerCaseButton.pack()
        self.__numberButton.pack()
        self.__specialCharacterButton.pack()
        self.__readableNoNumberButton.pack()
        self.__readableNumberButton.pack()
        self.__createPasswordButton.pack()
        self.__clearButton.pack()
        self.__window.mainloop()
