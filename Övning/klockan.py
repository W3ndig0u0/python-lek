hour = int(input("Klocka: "))
minutes = int(input("Minuter: "))
toAdd = int(input("Minuter att addera: "))

afterMidnight = hour * 60 + minutes + toAdd

# !Heltalsdivision
endHour = afterMidnight // 60

# !Procent är rest vid division
endMinutes = afterMidnight % 60

print("Sluttime : ", endHour)
print("Slutminuter : ", endMinutes)
