import random
import time


def main():
    # List of word's to use.
    words = ['pizza', 'love', 'life', 'amaizing', 'china', 'phone', 'color', 'chicken']
    # Choice's from the list above at random.
    word = (random.choice(words))
    # Prints the length of the word too guess.
    print("The word im thinking about is {} letter's long".format(len(word)))
    # Chances
    chances = 10
    # Where the incorrect guess is stored.
    done = []
    # Where the correct guess is stored.
    letters = []
    # Loops untill ......
    while chances > 0 and len(word) != len(letters):
        # Ask's the user for his guess.
        guess = str(input("Please input your guess: ")).lower()
        # Check's if the guess is in word and if not already in letters.
        if guess in word and guess not in letters:
            # Finds the letter's from guess in word.
            for i in word:
                # Make's i equal too guess.
                if i == guess:
                    letters.append(i)
                # Prints guessed letters in . else "-".
                print("{}".format(i if i in letters else "-"), end="")
            print()
        # Check's if guess in done then print's.
        elif guess in done:
            print("You Guessed that already")
        # Check's if guess not in word.
        elif guess not in word:
            # Adds the incorrect guess into done.
            done.append(guess)
            # Subtracts chances by 1.
            chances -= 1
            # Print's.
            print("You guessed wrong and have {} chance's left".format(chances))
    # Check's if chances are equal to 0 then print's.
    if chances == 0:
        print("You Lost")
    # If above is false print's......
    else:
        print("YOU WON!!!!!!!!!!!")
    # Ask's user if he would like to replay.
    replay = input("Please enter y to play again: ").lower()
    # Check's if replay is equal to y
    if replay == "y":
        print("Enjoy!")
        time.sleep(2.5)
        main()
    # If everything above false it break's
    else:
        print("Bye!")
main()
