from passwordGenerator import *
from passwordConfiguration import *
from tkinter import *

class PasswordConfigurationHandler():

    def createPasswordFromConfiguration(self, passwordConfiguration, passwordLength):
        generator = PasswordGenerator()
        if passwordConfiguration == PasswordConfiguration.UPPER_CASE:
            return str(generator.generateUpperCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE:
            return str(generator.generateLowerCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.NUMBER:
            return str(generator.generateNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.SPECIAL_CHARACTER:
            return str(generator.generateSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE:
            return str(generator.generateLowerUpperCasePassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_NUMBER:
            return str(generator.generateUpperCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER:
            return str(generator.generateUpperCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_NUMBER:
            return str(generator.generateLowerCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.NUMBER_SPECIAL_CHARACTER:
            return str(generator.generateNumberSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER:
            return str(generator.generateLowerCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_NUMBER:
            return str(generator.generateLowerUpperCaseNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER:
            return str(generator.generateLowerUpperCaseSpecialCharacterPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(generator.generateUpperCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(generator.generateLowerCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER_NUMBER:
            return str(generator.generateLowerUpperCaseSpecialCharacterNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.READABLE_NO_NUMBER:
            return str(generator.generateReadableNoNumberPassword(passwordLength))
        elif passwordConfiguration == PasswordConfiguration.READABLE_NUMBER:
            return str(generator.generateReadableNumberPassword(passwordLength))
