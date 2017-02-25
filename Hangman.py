#Defining a Function
def script():
    #imported the time module for the time.sleep(seconds)
    import time
    import string
    import random
    print("Welcome to hangman :)")
    list = ['pizza', 'love', 'daddy', 'stupid', 'fuck', 'jerk', 'asshole', 'chicken', 'nuggets', 'english', 'speakers']
    word = (random.choice(list))
    #Prints how long the word to guess is
    print("The word to guess is {} letter's :)".format(len(word)))
    chances = 10
    guesses = []
    first = 1
    while True:
        #If guesses equals to word
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
                print("Your input was invalid")
                break
        elif first > 0:
            guess = input("Please enter a letter guess: ").lower()
            first = (first - 1)
        elif chances > 0:
            guess = input("Please enter your next guess: ").lower()
            if guess not in string.ascii_lowercase:
                guess = input("Please enter a letter guess: ").lower()
        if guess in word and guess not in guesses:
                #checks how many (guess) are in (word) and adds to (guesses)
                for i in word:
                    if i == guess:
                        guesses.append(i)
                    print(" {} ".format(i if i in guesses else "_"), end="")
                print()
                #if all guessed print........{
                if len(guesses) == len(word):
                    print("You Guessed The Word CONGRATS!!!!")
                #else if len of guesses is not equal to word print ..........
            #else if the guess is already guessed print.........
        elif guess in guesses:
                print("You Already Guessed That")
            #else if guess is wrong decrease chances and print.....
        else:
                chances = (chances - 1)
                print("Your Guess Is Wrong")
                print("You Have {} Chances Left".format(chances))
        #if chances are less then 1 prints......
        if chances < 1:
            print("You lost sorry")
            script()
#Calling a Function
script()
