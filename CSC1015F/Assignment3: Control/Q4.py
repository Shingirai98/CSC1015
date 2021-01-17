# Row
# Shingirai Maburutse
# 09/01/21

month = input("Enter the month('January',...,'December'): ")
day = input("Enter the start day ('Monday',...,'Sunday': ")
print(month)
print("Mo Tu We Th Fr Sa Su")

start = 0

if day == "Monday": start = 0
elif day == "Tuesday": start = -1
elif day == "Wednesday": start = -2
elif day == "Thursday": start = -3
elif day == "Friday": start = -4
elif day == "Saturday": start = -5
elif day == "Sunday": start = -6
start += 1
ending = 30
if month == "January" or "March" or "May" or "July" or "August" or "October" or "December":
    ending = 31

if month == "February":
    ending = 28

for x in range(0,6):
    for i in range(0, 7):
        if start <= 0:
            print("  ", end=" ")

        else:
            print(f'{start:>2}', end=" ")

        start += 1

        if start > ending:
            break
    print()
    if start > ending:
        break







