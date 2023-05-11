import random
random=random.randrange(1,1000)

guesses=0

amt_of_guesses=1
for guess in range(1000):
    guess = int(input("Guess the number (from 1 to 1000): "))
    guesses = guesses + 1
    if guess == random:
        print("Correct!")
        break
    elif guess > random:
        print("Too high!")
    elif guess < random:
        print("Too low!")

print("Amount of guesses: ", guesses)
print("The correct answer is:", random)