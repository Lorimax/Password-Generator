from passwordGenerator import *
from passwordConfiguration import *
from tkinter import *

class PasswordConfigurationHandler():
    __generator = PasswordGenerator()

    def createPasswordFromConfiguration(self, passwordConfiguration, passwordLength):
        if passwordConfiguration == PasswordConfiguration.UPPER_CASE:
            return str(self.__generator.generateUpperCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE:
            return str(self.__generator.generateLowerCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.NUMBER:
            return str(self.__generator.generateNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.SPECIAL_CHARACTER:
            return str(self.__generator.generateSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE:
            return str(self.__generator.generateLowerUpperCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_NUMBER:
            return str(self.__generator.generateUpperCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER:
            return str(self.__generator.generateUpperCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_NUMBER:
            return str(self.__generator.generateLowerCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.NUMBER_SPECIAL_CHARACTER:
            return str(self.__generator.generateNumberSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER:
            return str(self.__generator.generateLowerCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_NUMBER:
            return str(self.__generator.generateLowerUpperCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER:
            return str(self.__generator.generateLowerUpperCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(self.__generator.generateUpperCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(self.__generator.generateLowerCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(self.__generator.generateLowerUpperCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.READABLE_NO_NUMBER:
            return str(self.__generator.generateReadableNoNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.READABLE_NUMBER:
            return str(self.__generator.generateReadableNumberPassword(passwordLength))
