# program to guess a secret number
# Shingirai Maburutse
# 08/01/21

secret_number = 42 # create secret number in program
guess = 0 # variable to store user's guess

# As long as we have not found the secret number
while guess != secret_number:
    # get a new guess from user
    guess = eval(input("What is the secret number?"))
    # Check if guess is too low
    if guess < secret_number:
        print("This is way too low. Please try again.")
    # or too high
    elif guess > secret_number:
        print("This is way too high. Please try again.")

print("Congratulations, you have guessed the correct number!")  # print message indicating success
