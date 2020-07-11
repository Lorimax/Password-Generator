from passwordGenerator import *
from passwordEvent import *
from tkinter import *

class PasswordEventHandler():
    __generator = PasswordGenerator()

    def executeEvent(self, passwordEvent, output):
        if passwordEvent == PasswordEvent.UPPER_CASE:
            output.insert(INSERT, str(self.__generator.generateUpperCasePassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_CASE:
            output.insert(INSERT, str(self.__generator.generateLowerCasePassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.NUMBER:
            output.insert(INSERT, str(self.__generator.generateNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.SPECIAL_CHARACTER:
            output.insert(INSERT, str(self.__generator.generateSpecialCharacterPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_UPPER_CASE:
            output.insert(INSERT, str(self.__generator.generateLowerUpperCasePassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.UPPER_CASE_NUMBER:
            output.insert(INSERT, str(self.__generator.generateUpperCaseNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.UPPER_CASE_SPECIAL_CHARACTER:
            output.insert(INSERT, str(self.__generator.generateUpperCaseSpecialCharacterPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_CASE_NUMBER:
            output.insert(INSERT, str(self.__generator.generateLowerCaseNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.NUMBER_SPECIAL_CHARACTER:
            output.insert(INSERT, str(self.__generator.generateNumberSpecialCharacterPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_CASE_SPECIAL_CHARACTER:
            output.insert(INSERT, str(self.__generator.generateLowerCaseSpecialCharacterPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_UPPER_CASE_NUMBER:
            output.insert(INSERT, str(self.__generator.generateLowerUpperCaseNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_UPPER_CASE_SPECIAL_CHARACTER:
            output.insert(INSERT, str(self.__generator.generateLowerUpperCaseSpecialCharacterPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            output.insert(INSERT, str(self.__generator.generateUpperCaseSpecialCharacterNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_CASE_SPECIAL_CHARACTER_NUMBER:
            output.insert(INSERT, str(self.__generator.generateLowerCaseSpecialCharacterNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.LOWER_UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            output.insert(INSERT, str(self.__generator.generateLowerUpperCaseSpecialCharacterNumberPassword(16)) + '\n')
        elif passwordEvent == PasswordEvent.READABLE_NO_NUMBER:
            output.insert(INSERT, str(self.__generator.generateReadableNoNumberPassword()) + '\n')
        elif passwordEvent == PasswordEvent.READABLE_NUMBER:
            output.insert(INSERT, str(self.__generator.generateReadableNumberPassword()) + '\n')
        output.pack()
