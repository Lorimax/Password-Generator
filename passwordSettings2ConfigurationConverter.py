from passwordSettings import *
from passwordConfiguration import *

class PasswordSettings2ConfigurationConverter():

    def __createConfigurationArray(self, settings):
        configurationArray = [0,0,0,0,0,0]
        if PasswordSettings.READABLE_NO_NUMBER in settings:
            return [0,0,0,0,1,0]
        if PasswordSettings.READABLE_NUMBER in settings:
            return [0,0,0,0,0,1]
        if PasswordSettings.UPPER_CASE in settings:
            configurationArray[0] = 1
        if PasswordSettings.LOWER_CASE in settings:
            configurationArray[1] = 1
        if PasswordSettings.NUMBER in settings:
            configurationArray[2] = 1
        if PasswordSettings.SPECIAL_CHARACTER in settings:
            configurationArray[3] = 1
        return configurationArray

    def convertSettings2Configuration(self, settings):
        configurationArray = self.__createConfigurationArray(settings)
        if configurationArray == [0,0,0,0,1,0]:
            return PasswordConfiguration.READABLE_NO_NUMBER
        elif configurationArray == [0,0,0,0,0,1]:
            return PasswordConfiguration.READABLE_NUMBER
        elif configurationArray == [1,0,0,0,0,0]:
            return PasswordConfiguration.UPPER_CASE
        elif configurationArray == [0,1,0,0,0,0]:
            return PasswordConfiguration.LOWER_CASE
        elif configurationArray == [0,0,1,0,0,0]:
            return PasswordConfiguration.NUMBER
        elif configurationArray == [0,0,0,1,0,0]:
            return PasswordConfiguration.SPECIAL_CHARACTER
        elif configurationArray == [1,1,0,0,0,0]:
            return PasswordConfiguration.LOWER_UPPER_CASE
        elif configurationArray == [1,0,1,0,0,0]:
            return PasswordConfiguration.UPPER_CASE_NUMBER
        elif configurationArray == [1,0,0,1,0,0]:
            return PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER
        elif configurationArray == [0,1,1,0,0,0]:
            return PasswordConfiguration.LOWER_CASE_NUMBER
        elif configurationArray == [0,0,1,1,0,0]:
            return PasswordConfiguration.NUMBER_SPECIAL_CHARACTER
        elif configurationArray == [0,1,0,1,0,0]:
            return PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER
        elif configurationArray == [1,1,1,0,0,0]:
            return PasswordConfiguration.LOWER_UPPER_CASE_NUMBER
        elif configurationArray == [1,1,0,1,0,0]:
            return PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER
        elif configurationArray == [1,0,1,1,0,0]:
            return PasswordConfiguration.UPPER_CASE_SPECIAL_CHARACTER_NUMBER
        elif configurationArray == [0,1,1,1,0,0]:
            return PasswordConfiguration.LOWER_CASE_SPECIAL_CHARACTER_NUMBER
        elif configurationArray == [1,1,1,1,0,0]:
            return PasswordConfiguration.LOWER_UPPER_CASE_SPECIAL_CHARACTER_NUMBER
