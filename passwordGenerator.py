import random

class PasswordGenerator():
    __upperCaseList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    __lowerCaseList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    __numberList = ['0','1','2','3','4','5','6','7','8','9']
    __specialCharacterList = ['!','@','#','$','%','^','&','*','(',')','-','?','_','{','}','[',']',',','<','>','.','\"','\'','/','\\']

    def generateUpperCasePassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            password.append(str(random.choice(self.__upperCaseList)))
        return ''.join(password)

    def generateLowerCasePassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            password.append(str(random.choice(self.__lowerCaseList)))
        return ''.join(password)

    def generateNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            password.append(str(random.choice(self.__numberList)))
        return ''.join(password)

    def generateSpecialCharacterPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)

    def generateLowerUpperCasePassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__upperCaseList)))
            else:
                password.append(str(random.choice(self.__lowerCaseList)))
        return ''.join(password)


    def generateUpperCaseNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__upperCaseList)))
            else:
                password.append(str(random.choice(self.__numberList)))
        return ''.join(password)


    def generateUpperCaseSpecialCharacterPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__upperCaseList)))
            else:
                password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)

    def generateLowerCaseNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__lowerCaseList)))
            else:
                password.append(str(random.choice(self.__numberList)))
        return ''.join(password)

    def generateNumberSpecialCharacterPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__numberCaseList)))
            else:
                password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)


    def generateLowerCaseSpecialCharacterPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            if  bool(random.getrandbits(1)):
                password.append(str(random.choice(self.__lowerCaseList)))
            else:
                password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)


    def generateLowerUpperCaseNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            listChoice = random.randint(0,2)
            if listChoice == 0:
                password.append(str(random.choice(self.__upperCaseList)))
            elif listChoice == 1:
                password.append(str(random.choice(self.__lowerCaseList)))
            else:
                password.append(str(random.choice(self.__numberList)))
        return ''.join(password)

    def generateLowerUpperCaseSpecialCharacterPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            listChoice = random.randint(0,2)
            if listChoice == 0:
                password.append(str(random.choice(self.__upperCaseList)))
            elif listChoice == 1:
                password.append(str(random.choice(self.__lowerCaseList)))
            else:
                password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)

    def generateUpperCaseSpecialCharacterNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            listChoice = random.randint(0,2)
            if listChoice == 0:
                password.append(str(random.choice(self.__upperCaseList)))
            elif listChoice == 1:
                password.append(str(random.choice(self.__specialCharacterList)))
            else:
                password.append(str(random.choice(self.__numberList)))
        return ''.join(password)

    def generateLowerCaseSpecialCharacterNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            listChoice = random.randint(0,2)
            if listChoice == 0:
                password.append(str(random.choice(self.__lowerCaseList)))
            elif listChoice == 1:
                password.append(str(random.choice(self.__specialCharacterList)))
            else:
                password.append(str(random.choice(self.__numberList)))
        return ''.join(password)

    def generateLowerUpperCaseSpecialCharacterNumberPassword(self, passwordLength):
        password = []
        for i in range(passwordLength):
            listChoice = random.randint(0,3)
            if listChoice == 0:
                password.append(str(random.choice(self.__upperCaseList)))
            elif listChoice == 1:
                password.append(str(random.choice(self.__lowerCaseList)))
            elif listChoice == 2:
                password.append(str(random.choice(self.__numberList)))
            else:
                password.append(str(random.choice(self.__specialCharacterList)))
        return ''.join(password)

    def generateReadableNoNumberPassword(self, passwordLength):
        vowels = ['a','e','i','o','u','y']
        consonants = ['b','c','d','f','g','h','k','l','m','n','p','q','r','s','t','v','w','x','z']
        readableTwoConsonantCombinations = ['sp','th','sh','ch','fr','wh']
        password = []
        charactersWritten = 0
        listChoice = random.randint(0,2)
        while charactersWritten < passwordLength:
            if listChoice == 0: #append vowel
                password.append(str(random.choice(vowels)))
                charactersWritten += 1
                listChoice = random.randint(1,2)
            elif listChoice == 1: #append consonant
                password.append(str(random.choice(consonants)))
                charactersWritten += 1
                listChoice = 0
            elif listChoice == 2: #append consonant combination
                if (passwordLength - charactersWritten) > 2: #check for enough space
                    password.append(str(random.choice(readableTwoConsonantCombinations)))
                    charactersWritten += 2
                else: #append single constant if not enough space for consonant combination
                    password.append(str(random.choice(consonants)))
                    charactersWritten += 1
                listChoice = 0
        return ''.join(password)

    def generateReadableNumberPassword(self, passwordLength):
        password = []
        if passwordLength < 5:
            return self.generateNumberPassword(passwordLength)
        numberDigits = random.randint(1,4)
        numbers = self.generateNumberPassword(numberDigits)
        putNumbersFirst = bool(random.getrandbits(1))
        if putNumbersFirst:
            password.append(numbers)
            password.append(str(self.generateReadableNoNumberPassword(passwordLength - numberDigits)))
        else:
            password.append(str(self.generateReadableNoNumberPassword(passwordLength - numberDigits)))
            password.append(numbers)
        return ''.join(password)
