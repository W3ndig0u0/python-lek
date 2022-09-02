
# !Impoterar Biblotek
import random
import collections

# !Definerar varibler
welcome = "välkommmen"
name = "vad är ditt namn"
ques = "Vilka två heltal vill du slumpa en siffra mellan"
ques2 = "Hejsan,"

nameAnswer = None
firstNum = None
secNum = None


# !Funktioner

# ?Borde ha en funktion för att skriva ett tal allmänt istället för en som tar 2,
# ?Det blir mer flexibel och lättare då.

def chooseNumber(num1, num2):
    numList = []
    num1 = int(input("Vad är det första talet du väljer? "))
    num2 = int(input("Vad är det andra talet du väljer? "))
    numList.insert(num1, num2)
    return numList


# !Logik
print(welcome)
print(name)

nameAnswer = input()

print(ques2, nameAnswer)
print(ques)

# chooseNumber(firstNum, secNum)
print(chooseNumber(firstNum, secNum))

# if firstNum >= secNum:
# print("Din första tal måste vara mindre än den andra talet")


randomNumber = random.randint(firstNum, secNum)

print(randomNumber)
