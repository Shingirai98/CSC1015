# pi
# Shingirai Maburutse
# 08/01/21
import math

# initial pi value
pi = 2

# initial denominator
x = math.sqrt(2)

# for the fraction to be 1, the denominator has to be the same as the numerator ie. 2
while (x!=2):
    pi = pi * 2/x
    x = math.sqrt(2+x)

print("Approximation to pi(unrounded):", pi)
print("Approximation to pi(rounded):", round(pi, 3))
radius = eval(input("Enter the radius:\n"))
Area = pi * (radius ** 2)
print("Area:", round(Area, 3))
