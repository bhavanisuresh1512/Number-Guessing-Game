import random
number = random.randint(1, 100)

print(" Welcome to Number Guessing Game!")
print("Guess a number between 1 and 100")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low! Try again.")
    elif guess > number:
        print("Too High! Try again.")
    else:
        print("Correct Guess!")
        print("You guessed the number in", attempts, "attempts.")
        break























