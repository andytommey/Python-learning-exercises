"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

a = random.randint(1, 9)

guess = int(input("Guess what number I'm thinking of, between 1 and 9: "))

if a == guess:
    print("Wow, you guessed exactly right!")
elif a > guess:
    print("Nope, too low!")
else:
    print("Nope, too high!")
