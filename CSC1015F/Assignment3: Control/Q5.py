# Palindrome primes
# Shingirai Maburutse
# 17/01/21

num1 = eval(input("Enter first number:\n"))
num2 = eval(input("Enter second number:\n"))

# A palindrome number is a number that reads the same from the front and the back.
# Examples are: 212, 44, 9009, 4567654.

# Reverse the number

# ------------------Function to calculate the length of the number--------------------------------
def leng(num):

    length = 0
    while num != 0:
        num = num // 10
        length += 1

    return length

# ------------------------------------------------------------------------------------------------

# ------------------Function to reverse number----------------------------------------------------
def reverse(num):
    l = leng(num)
    temp = 0
    final = 0
    for i in range(l):
        temp = num % 10
        num = num // 10
        final = final + temp * (10 ** (l-1))
        l -= 1

    return final

# --------------------------------------------------------------------------------------------------

# ------------------Function to check if number is palindrome----------------------------------------------------
def pali(num):
    rev = reverse(num)
    if num == rev:
        return True
    else:
        return False

# --------------------------------------------------------------------------------------------------

# ------------------Function to check if number is prime----------------------------------------------------
def prime(num):
    counter = 0
    for i in range(1, num):
        if num % i == 0:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False
# --------------------------------------------------------------------------------------------------

# Printing palindroming primes in a range of values
print("The palindromic primes are:")
num = num1
while num != num2+1:
    if pali(num) and prime(num):
        print(num)
        num += 1
    else:
        num += 1
        continue
