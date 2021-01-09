# Column
# Shingirai Maburutse
# 09/01/21

start = eval(input("Enter the start number: "))

if -6 < start < 93:
    for i in range(0, 6):
        print(f'{start:>2}', end="\n")
        start += 7
