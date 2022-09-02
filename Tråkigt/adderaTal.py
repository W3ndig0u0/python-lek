tal = int(input("Tal: "))
summa = 0
biggestNr = -1
medium = 0
loopNr = 0

while tal >= 0:
    print(tal)
    loopNr += 1
    summa += tal

    if biggestNr <= tal:
        biggestNr = tal

    tal = int(input("Tal: "))

    medium = summa / loopNr

print("Loop nummer: ", loopNr)
print("Medium: ", medium)
print("Största talet: ", biggestNr)
print("Summa: ", summa)
