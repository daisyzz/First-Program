import random
import time

words = ["airplane", "pizza", "grandma", "mother", "flags", "countries"]

print("Welcome to HangMan by Owen!")
print("When stuck use 'HELP!' :)")


def main(lives, helps):
    if len(words) < 1:
        print("You tried all of our word's congrats!!!!!")
        print("Exiting in 10 second's! Thank you for playing")
        time.sleep(10)
        quit()

    word = random.choice(words).lower()
    words.remove(word)
    correct = []
    wrong = []
    left = []

    for h in word:
        left.append(h)

    while lives > 0 and len(correct) != len(word):
        guess = input("Guess a letter: ").lower()

        if guess == "help!" and helps > 0:
            choice = input("Would you like to sacrifice a life for a letter 'Only one use per word' Y/N: ").lower()
            if choice == "y":
                stuck = random.choice(left)
                helps -= 1
                lives -= 1
                print("Your letter is '{}' and are left with {} {}".format(stuck, lives, "lives" if lives > 1 else "life"))
                continue
            else:
                continue

        if guess.isdigit() or len(guess) != 1:
            print("Only a letter guess.")
            continue

        if guess in correct or guess in wrong:
            print("You've already tried '{}', and it was {}!".format(guess, "correct" if guess in correct else"wrong"))
        elif guess in word:
            for i in word:
                if i in guess:
                    correct.append(i)
                    left.remove(i)
                print("{} ".format(i if i in correct else"_"), end="")
            print()
        else:
            print("Nope, There's no '{}' in it!".format(guess))
            wrong.append(guess)
            lives -= 1
            print("You have {} {} left!".format(lives, "lives" if lives > 1 else "life"))
    if lives < 1:
        print("You Lost! it was {}".format(word))
    else:
        print("You Won!!!!")
    restart = input("Would you like a new word Y/N: ").lower()

    if restart == "y":
        main(5, 1)
    else:
        print("Exiting in 10 second's! Thank you for playing")
        time.sleep(10)
main(5, 1)
