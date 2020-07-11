from tkinter import *
from passwordConfigurationHandler import *
from passwordConfiguration import *
from passwordSettings import *
from passwordSettings2ConfigurationConverter import *

class GUI():
    __window = Tk()
    __passwordSettings = []
    __passwordLengthLabel = Label(None, text='Password length')
    __passwordLengthEntry = Entry(None)
    __upperCaseButton = Button(None, text='Upper case characters')
    __lowerCaseButton = Button(None, text='Lower case characters')
    __numberButton = Button(None, text='Numbers')
    __specialCharacterButton = Button(None, text='Special characters')
    __readableNoNumberButton = Button(None, text='Readable without numbers')
    __readableNumberButton = Button(None, text='Readable with numbers')
    __createPasswordButton = Button(None, text='Create Password')
    __clearButton = Button(None, text='Clear')

    def __isCorrectPasswordLength(self):
        try:
            self.__setPasswordLength()
            if self.__passwordLength > 0:
                return True
            else:
                self.__drawWrongPasswordLength()
                return False
        except:
            self.__drawWrongPasswordLength()
            return False

    def __setPasswordLength(self):
        self.__passwordLength = int(self.__passwordLengthEntry.get())

    def __createPassword(self, event):
        if not self.__passwordSettings:
            self.__drawNothingSelected()
        elif self.__isCorrectPasswordLength():
            settingsConverter = PasswordSettings2ConfigurationConverter()
            configurationHandler = PasswordConfigurationHandler()
            passwordConfiguration = settingsConverter.convertSettings2Configuration(self.__passwordSettings)
            password = configurationHandler.createPasswordFromConfiguration(passwordConfiguration, self.__passwordLength)
            self.__drawPassword(password)

    def __drawWrongPasswordLength(self):
        self.__output.insert(INSERT, "Invalid password length!\n")
        self.__output.pack()

    def __drawNothingSelected(self):
        self.__output.insert(INSERT, "Nothing selected!\n")
        self.__output.pack()

    def __drawPassword(self, password):
        self.__output.insert(INSERT, str(password) + '\n')
        self.__output.pack()

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
        self.__output.delete('1.0', END)

    def __drawSetting(self,setting):
        if setting == PasswordSettings.UPPER_CASE:
            self._output.insert(INSERT, "Upper case characters selected\n")
            self._output.pack()
        elif setting == PasswordSettings.LOWER_CASE:
            self._output.insert(INSERT, "Lower case characters selected\n")
            self._output.pack()
        elif setting == PasswordSettings.NUMBER:
            self._output.insert(INSERT, "Numbers selected\n")
            self._output.pack()
        elif setting == PasswordSettings.SPECIAL_CHARACTER:
            self._output.insert(INSERT, "Special characters selected\n")
            self._output.pack()
        elif setting == PasswordSettings.READABLE_NO_NUMBER:
            self._output.insert(INSERT, "Readable without numbers selected\n")
            self._output.pack()
        elif setting == PasswordSettings.READABLE_NUMBER:
            self._output.insert(INSERT, "Readable with numbers selected\n")
            self._output.pack()

    def __bindButtons(self):
        self.__upperCaseButton.bind('<Button-1>', self.__setUpperCase)
        self.__lowerCaseButton.bind('<Button-1>', self.__setLowerCase)
        self.__numberButton.bind('<Button-1>', self.__setNumber)
        self.__specialCharacterButton.bind('<Button-1>', self.__setSpecialCharacter)
        self.__createPasswordButton.bind('<Button-1>', self.__createPassword)
        self.__readableNoNumberButton.bind('<Button-1>', self.__setReadableNoNumber)
        self.__readableNumberButton.bind('<Button-1>', self.__setReadableNumber)
        self.__clearButton.bind('<Button-1>', self.__clear)
        self.__passwordLengthEntry.bind()

    def __packButtons(self):
        self.__passwordLengthLabel.pack()
        self.__passwordLengthEntry.pack()
        self.__upperCaseButton.pack()
        self.__lowerCaseButton.pack()
        self.__numberButton.pack()
        self.__specialCharacterButton.pack()
        self.__readableNoNumberButton.pack()
        self.__readableNumberButton.pack()
        self.__createPasswordButton.pack()
        self.__clearButton.pack()

    def draw(self):
        self.__output = Text(self.__window)
        self.__bindButtons()
        self.__packButtons()
        self.__window.mainloop()
