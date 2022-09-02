skala = input("Skala: ")


# !Celse => Fahr
def CelsConverter():
    print("Du valde Farenheit till Celsius")
    cels = float(input("Grader Celsius: "))
    fahr = cels * 1.8 + 32
    print("grader fahrenheit ", fahr)


# !Fahr => Cels
def FahrConverter():
    print("Du valde Celsuis till Farenheit")
    fahr = float(input("Fahrenheit: "))
    cels = (fahr - 32) / 1.8
    print("grader Celsius ", cels)


# !Logik
if skala == "Farenheit":
    CelsConverter()
elif skala == "Celsius":
    FahrConverter()
else:
    print("Du valde inte Celsuis eller Farenheit")

print("bye")
