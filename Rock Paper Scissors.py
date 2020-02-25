"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)"""

playerOne = input("Player one: Rock, paper, or scissors?: ")
playerTwo = input("Player two: Rock, paper, or scissors?: ")
playerOne = playerOne.lower()
playerTwo = playerTwo.lower()

while True:
    if playerOne == 'rock' and playerTwo == 'scissors':
        print("Player One wins, congratulations!")
    elif playerOne == 'rock' and playerTwo == 'paper':
        print("Player Two wins. Congratulations!")
    elif playerOne == 'rock' and playerTwo == 'rock':
        print("It's a draw!")
    elif playerOne == 'paper' and playerTwo == 'scissors':
        print("Player Two wins. Congratulations!")
    elif playerOne == 'paper' and playerTwo == 'rock':
        print("Player Two wins. Congratulations!")
    elif playerOne == 'paper' and playerTwo == 'paper':
        print("It's a draw!")
    elif playerOne == 'scissors' and playerTwo == 'rock':
        print("Player Two wins. Congratulations!")
    elif playerOne == 'scissors' and playerTwo == 'paper':
        print("Player Two wins. Congratulations!")
    elif playerOne == 'scissors' and playerTwo == 'scissors':
        print("It's a draw!")
    else:
        print("Whoops! Something went wrong.")

    ask = input("Would you like to play again? y/n: ")
    if ask == 'n':
        print("Thanks for playing!")
        break
    else:
        playerOne = input("Player one: Rock, paper, or scissors?: ")
        playerTwo = input("Player two: Rock, paper, or scissors?: ")
        playerOne = playerOne.lower()
        playerTwo = playerTwo.lower()
