def script():
    import time
    word = str(input("Please Enter a Word: "))
    print("The Word's Length is {} Letter's :)".format(len(word)))
    chances = 10
    guesses = []
    y = "Y"
    n = "N"
    while True:
        if len(guesses) == len(word):
            print("YOU WON!!!!!!!")
            time.sleep(2.5)
            replay = input("Would You Like To Play Again Y/N: ")
            if replay == y:
                script()
            elif replay == n:
                print("Okay Bye")
                break
            else:
                print("Your Input Was Invalid")
                break
        elif chances > 0:
            guess = input("Please Enter Your Guess: ")
            if guess in word and guess not in guesses:
                guesses.append(guess)
                print("You Guessed {} So Far".format(len(guesses)))
                print("You Have {} Left To Guess".format(len(word) - len(guesses)))
            elif guess in guesses:
                print("You Already Guessed That")
            else:
                chances = (chances - 1)
                print("Your Guess Is Wrong")
                print("You Have {} Chances Left".format(chances))
        elif chances < 1:
            print("You Lost :) Sorry")
            script()
script()
