"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

a = random.randint(1, 9)

guess = int(input("Guess what number I'm thinking of, between 1 and 9: "))
count = 0
while True:
    if a == guess:
        print("Wow, you guessed exactly right!")
    elif a > guess:
        print("Nope, too low!")
    else:
        print("Nope, too high!")
    count += 1
    leaveGame = input("Type 'exit' if you wish to quit the game. If not, just press enter: ")
    leaveGame = leaveGame.lower()
    if leaveGame == 'exit':
        break
    else:
        guess = int(input("Guess what number I'm thinking of, between 1 and 9: "))

print("Thanks for playing. It took you " + str(count) + " guesses to get right!")
