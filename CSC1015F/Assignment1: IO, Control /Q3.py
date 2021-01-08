# Time validity
# Shingirai Maburutse
# 08/01/2020

hours = eval(input("Enter the hours:"))
minutes = eval(input("Enter the minutes:"))
seconds = eval(input("Enter the seconds:"))

if (0 <= hours < 24) and (0 <= minutes < 60) and (0 <= seconds < 60):
    print("Your time is valid.")

else:
    print("Your time is invalid.")