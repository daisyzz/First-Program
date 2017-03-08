def script():
    #imported the time module for the time.sleep(seconds)
    import time
    import string
    import random
    print("Welcome To The Game Of HangMan")
    list_guesses = ['pizza', 'love', 'daddy', 'stupid', 'fuck', 'jerk', 'asshole', 'chicken', 'nuggets', 'english', 'speakers']
    word = (random.choice(list_guesses))
    print("The word to guess is {} letter's :)".format(len(word)))
    chances = 10
    guesses = []
    gussed = []
    while chances > 0:
        if chances != 5 and chances > 1 and len(guesses) != len(word):
            guess = input("Please enter a letter guess: ").lower()
        if guess not in string.ascii_lowercase or len(guess) > 1:
            continue
        if len(guesses) == len(word):
            print("YOU WON!!!!!!!")
            time.sleep(2.5)
            replay = input("Would you like to play again Y/N: ").lower()
            if replay == "y":
                script()
            elif replay == "n":
                print("Okay Bye")
                break
            else:
                print("Please Enter Y/N")
        if chances == 5:
            left = ""
            for letter in word:
                if letter not in guesses:
                    left = left + letter
            hint = input("Would you like a hint Y/N: ").lower()
            if hint == "y":
                hintz = format(random.choice(left))
                for l in word:
                    if l == hintz:
                        guesses.append(l)
                    print(" {} ".format(l if l in guesses else "_"), end="")
                print()
                print("The hint was {}".format(hintz))
                chances = (chances - 1)
                continue
            elif hint == "n":
                print("Okay good luck")
                continue
        if guess in word and guess not in guesses:
            """checks how many (guess) are in (word) and adds to (guesses)"""
            for i in word:
                if i == guess:
                    guesses.append(i)
                print(" {} ".format(i if i in guesses else "_"), end="")
            print()
            """if all guessed print........"""
            if len(guesses) == len(word):
                print("You Guessed The Word CONGRATS!!!!")
            """else if the guess is already guessed print........."""
        elif guess in guesses or guess in gussed:
            print("You Already Guessed That")
            """else if guess is wrong decrease chances and print....."""
        elif guess not in word:
            gussed.append(guess)
            chances = (chances - 1)
            print("You guessed wrong")
            print("You have {} chances left".format(chances))
            """if chances are less then 1 prints......"""
script()
