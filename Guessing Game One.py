"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

a = random.randint(1, 9)
guess = int(input("Guess what number I'm thinking of, between 1 and 9: "))
count = 1
while True:
    if a == guess:
        print("That's correct!")
        break
    elif a > guess:
        print("Nope, too low!")
    elif a < guess < 10:
        print("Nope, too high!")
    else:
        print("Whoops, that's not a number between 1 and 9")

    count += 1
    leaveGame = input("Press enter to try again, or type 'exit' if you wish to quit the game: ")
    leaveGame = leaveGame.lower()
    if leaveGame == 'exit':
        break
    else:
        guess = int(input("Guess what number I'm thinking of, between 1 and 9: "))


if count == 1:
    print("Wow, you got it in one, Amazing guess!")
elif 1 < count < 5:
    print("You got it in " + str(count) + " tries, nice job!")
elif 4 < count < 9:
    print("You got it in " + str(count) + " tries, that's ok I guess.")
else:
    print(str(count) + " guesses huh? That's a lot. Try harder next time.")
