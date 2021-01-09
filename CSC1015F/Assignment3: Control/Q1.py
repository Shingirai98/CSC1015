# Row
# Shingirai Maburutse
# 09/01/21

start = eval(input("Enter the start number:\n"))

if -6 < start < 93:
    for i in range(0, 7):
        print(f'{start:>2}', end=" ")
        start += 1
