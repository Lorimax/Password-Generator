from passwordSettings import *
from passwordEvent import *

class PasswordSettings2EventConverter():
    def __createSettingArray(self, settings):
        settingArray = [0,0,0,0,0,0]
        if PasswordSettings.READABLE_NO_NUMBER in settings:
            return [0,0,0,0,1,0]
        if PasswordSettings.READABLE_NUMBER in settings:
            return [0,0,0,0,0,1]
        if PasswordSettings.UPPER_CASE in settings:
            settingArray[0] = 1
        if PasswordSettings.LOWER_CASE in settings:
            settingArray[1] = 1
        if PasswordSettings.NUMBER in settings:
            settingArray[2] = 1
        if PasswordSettings.SPECIAL_CHARACTER in settings:
            settingArray[3] = 1
        return settingArray

    def convertSettings2Event(self, settings):
        settingArray = self.__createSettingArray(settings)
        if settingArray == [0,0,0,0,1,0]:
            return PasswordEvent.READABLE_NO_NUMBER
        elif settingArray == [0,0,0,0,0,1]:
            return PasswordEvent.READABLE_NUMBER
        elif settingArray == [1,0,0,0,0,0]:
            return PasswordEvent.UPPER_CASE
        elif settingArray == [0,1,0,0,0,0]:
            return PasswordEvent.LOWER_CASE
        elif settingArray == [0,0,1,0,0,0]:
            return PasswordEvent.NUMBER
        elif settingArray == [0,0,0,1,0,0]:
            return PasswordEvent.SPECIAL_CHARACTER
        elif settingArray == [1,1,0,0,0,0]:
            return PasswordEvent.LOWER_UPPER_CASE
        elif settingArray == [1,0,1,0,0,0]:
            return PasswordEvent.UPPER_CASE_NUMBER
        elif settingArray == [1,0,0,1,0,0]:
            return PasswordEvent.UPPER_CASE_SPECIAL_CHARACTER
        elif settingArray == [0,1,1,0,0,0]:
            return PasswordEvent.LOWER_CASE_NUMBER
        elif settingArray == [0,0,1,1,0,0]:
            return PasswordEvent.NUMBER_SPECIAL_CHARACTER
        elif settingArray == [0,1,0,1,0,0]:
            return PasswordEvent.LOWER_CASE_SPECIAL_CHARACTER
        elif settingArray == [1,1,1,0,0,0]:
            return PasswordEvent.LOWER_UPPER_CASE_NUMBER
        elif settingArray == [1,1,0,1,0,0]:
            return PasswordEvent.LOWER_UPPER_CASE_SPECIAL_CHARACTER
        elif settingArray == [1,0,1,1,0,0]:
            return PasswordEvent.UPPER_CASE_SPECIAL_CHARACTER_NUMBER
        elif settingArray == [0,1,1,1,0,0]:
            return PasswordEvent.LOWER_CASE_SPECIAL_CHARACTER_NUMBER
        elif settingArray == [1,1,1,1,0,0]:
            return PasswordEvent.LOWER_UPPER_CASE_SPECIAL_CHARACTER_NUMBER
