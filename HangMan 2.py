import random
import time

commands = ['start', 'easy', 'quit']
words = ['pizza', 'lemon', 'orange']


def start():
    print("""
HangMan by Owen
Commands
start - to get a word
easy - play extra lives
quit - exit the game""")
    if len(words) < 1:
        print("You tried all of our word's congrats!!!!!")
        print("Exiting in 10 second's! Thank you for playing")
        time.sleep(10)
        quit()
    command = input(">").lower()
    if command == 'start':
        main(3)
    elif command == 'easy':
        main(6)
    elif command == 'quit':
        quit()
    else:
        print("I don't understand")


def main(lives):
    word = random.choice(words)
    print(f'Your word is {len(word)} characters')
    words.remove(word)
    right_guess = ''
    wrong_guess = ''
    while lives > 0 and len(word) != len(right_guess):
        player_input = input("Please enter your guess: ").lower()
        if player_input is not type(str) and len(player_input) != 1:
            print("Only single letter guesses please.")
        elif player_input in right_guess or player_input in wrong_guess:
            print("You already guessed that!")
        elif player_input in word:
            print("You got it right!")
            for i in word:
                if i == player_input:
                    right_guess += i
                print(f'{i if i in right_guess else"_"} ', end='')
            print()
        else:
            lives -= 1
            wrong_guess += player_input
            print(f"You guess is wrong and now have {lives} {'life' if lives == 1 else 'lives'} left.")
    print(f"You {'won' if lives > 1 else 'lost'} with {lives} {'life' if lives == 1 else 'lives'} left")
    start()


start()
