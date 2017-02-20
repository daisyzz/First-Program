guess = (input("Player One Please Input Your Word For Player 2 Too Guess: "))
guesses = []
chances = 10
print("The Word You Need To Guess is {} LettersLong".format(len(guess)))
while True:
    if len(guesses) == len(guess):
        print("You win")
        print("Would you like to play again")
        answer = input("Y/N: ")
        if answer == "y" or "yes":
            chances = (chances + 10)
            guesses = []
            guess = (input("Player One Please Input Your Word For Player 2 Too Guess: "))
            continue
        else:
            break
    elif chances > 0:
        y_guess = input("Player Two Please Enter Your Guess: ")
    elif chances < 1:
        print("You Lose")
        break
    if y_guess in guess and y_guess not in guesses:
        print("You Guessed a letter")
        guesses.append(y_guess)
        print("you have guessed {} letter".format(len(guesses)))
        print(guesses)
    elif y_guess in guesses:
        print("you already guessed that")
    else:
        chances = (chances - 1)
        print("u Guessed wrong")
        print("you have {} chances left".format(chances))
