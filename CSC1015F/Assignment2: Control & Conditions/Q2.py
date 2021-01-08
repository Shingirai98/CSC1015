# First day of the year
# Shingirai Maburutse
# 08/01/21

first = eval(input("Enter first year\n"))
second = eval(input("Enter the second year:\n"))

while(first <= second):
    day = (1+5*((first-1) % 4)+ 4*((first-1)% 100) + 6 * ((first-1) % 400)) % 7

    if (day==0):
        a = "Sunday"

    elif(day==1):
        a = "Monday"
    elif (day == 2):
        a = "Tuesday"
    elif (day == 3):
        a = "Wednesday"
    elif (day == 4):
        a = "Thursday"
    elif (day == 5):
        a = "Friday"
    else:
        a = "Saturday"

    print("The 1st of January", first, "falls on a", a, end=".\n")
    first=first+1

