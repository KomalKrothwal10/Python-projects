import random

# Generate a random number between 1 and 100
n = random.randint(1, 100)
a = -1
guesses = 0

while a != n:
    guesses += 1
    # Ask the user to guess the number
    a = int(input("Guess the number between 1 and 100: "))
    
    # Provide feedback based on the user's guess
    if a > n:
        print("Lower number, please.")
    elif a < n:
        print("Higher number, please.")
    else:
        print(f"Congratulations! You guessed the number correctly in {guesses} attempts.")
