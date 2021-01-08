# Triangle area calculation
# Shingirai Maburutse
# 08/01/21

import math

a = eval(input("Enter the length of the first side: "))
b = eval(input("Enter the length of the second side: "))
c = eval(input("Enter the length of the third side: "))

s = (a+b+c) / 2
x = s*(s-a)*(s-b)*(s-c)
Area = math.sqrt(x)

print("The area of the triangle with sides of length ",a,", ",b," and ", c, " is ", Area, sep="")