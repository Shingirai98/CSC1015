# Grid
# Shingirai Maburutse
# 09/01/21

start = eval(input("Enter the start number:"))

if -6 < start < 2:
    for x in range(0, 6):
        for i in range(0, 7):
            print(f'{start:>2}', end=" ")
            start += 1

        print("")
