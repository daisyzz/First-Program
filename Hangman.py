import time
print("Welcome To HangMan :)")
guess = (input("Player One Please Input Your Word For Player 2 Too Guess: "))
guesses = []
chances = 10
y = "y"
n = "n"

print("The Length of The Word You Need To Guess is {}".format(len(guess)))
while True:
    if len(guesses) == len(guess):
        print("You Win!!!!!!!!!")
        print("Would You Like To Play Again")
        answer = str(input("y/n: "))
        if answer == y:
            chances = 10
            guesses = []
            guess = (input("Player One Please Input Your Word For Player 2 Too Guess: "))
            continue
        elif answer == n:
            print("Bye :)")
            time.sleep(5)
            break
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
        print("you have guessed {} letter's".format(len(guesses)))
        print(guesses)
    elif y_guess in guesses:
        print("you already guessed that letter")
    else:
        chances = (chances - 1)
        print("Your Guess is invalid")
        print("you have {} chances left".format(chances))
