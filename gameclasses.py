class Game():

    def __init__(self, noOfQuestions = 0):
        self._noOfQuestions = noOfQuestions
        #self._noOfQuestions = 0

    @property
    def noOfQuestions(self):
        return self._noOfQuestions

    @noOfQuestions.setter
    def noOfQuestions(self, value):
        if value < 1:
            self._noOfQuestions = 1
            print("\nMinimalna ilosc pytan to 1\nWiec ilosc pytan ustawiam na 1\n")
        elif value > 10:
            self._noOfQuestions = 10
            print("\nMaksymalna ilos pytan to 10\nWiec ilosc pytan ustawiam na 10\n")
        else:
            self._noOfQuestions = value

class BinaryGame(Game):
    def generateQuestions(self):
        import random
        score = 0
        for i in range(self.noOfQuestions):
            base10 = random.randint(1, 100)
            print(base10)
            print("Podaj wynik:\n")
            userResult = input()
            while True:
                try:
                    answer = int(userResult, base = 2)
                    if answer == base10:
                        print("Zgadza sie!")
                        score += 1
                        break
                    else:
                        print("Zla odpowiedz, poprawna to: {:b}.\n".format(base10))
                        break
                except:
                    print("To nie jest liczba binarna. Jeszcze raz:\n")
                    #answer1 = int(userResult, base = 2)
                    print("Podaj wynik:\n")
                    userResult = input()
        return score

class MathGame(Game):
    def generateQuestions(self):
        import random
        score = 0
        numberList = [0, 0, 0, 0, 0]
        symbolList = ["", "", "", ""]
        operatorDict = {1:"+", 2:"-", 3:"*", 4:"**"}
        c = 0
        d = 0
        e = 0
        f = 1
        questionString = []
        for i in range(self.noOfQuestions):
            for x in numberList:
                numberList[c] = random.randint(1, 9)
                c += 1
            for x in symbolList:
                symbolList[d] = operatorDict[random.randint(1, 4)]
                if symbolList[d - 1] == operatorDict[4] and symbolList[d] == operatorDict[4]:
                    symbolList[d] = operatorDict[random.randint(1, 3)]
                d += 1
            questionString = str(numberList[0])
            for x in range(1, len(numberList)+len(symbolList)):
                if x % 2 != 0:
                    questionString = questionString + str(symbolList[e])
                    e += 1
                else:
                    questionString = questionString + str(numberList[f])
                    f += 1
            result = eval(questionString)
            questionString = questionString.replace('**', '^')
            print(questionString)
            print("Podaj wynik:\n")
            userResult = input()
            while True:
                try:
                    answer = int(userResult)
                    if answer == result:
                        print("Zgadza sie!")
                        score += 1
                        break
                    else:
                        print("Zla odpowiedz, poprawna to: {:d}.\n" .format(result))
                        break
                except:
                    print("To nie jest integer. Jeszcze raz:\n")
                    #answer1 = int(userResult)
                    print("Podaj wynik:\n")
                    userResult = input()
            return score






