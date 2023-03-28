import random
random = random.randrange(1,5)

for guess in range(3):
    guess = int(input("Guess the number (from 1 to 5): "))
    if guess == random:
        print("Correct!")
        break
    elif guess > random:
        print("Too high!")
    elif guess < random:
        print("Too low!")

print("The correct answer is:", random)