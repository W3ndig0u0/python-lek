
hour = int(print("Klocka: "))
minutes = int(print("Minuter: "))
toAdd = int(print("Minuter att addera: "))

afterMidnight = hour * 60 + minutes + toAdd

# !Heltalsdivision
endHour = afterMidnight // 60

# !Procent är rest vid division
endMinutes = afterMidnight % 60

print("Sluttime : ", endHour)
print("Slutminuter : ", endMinutes)
