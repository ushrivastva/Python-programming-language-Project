# Hangman in Python 
from wordlist import words
import random


# dictionary of key:()
hangman_art = {0:("___________",
                  "           ",
                  "           ",
                  "           ",
                  "           "),
               1:("___________",
                  "        O  ",
                  "           ",
                  "           ",
                  "           "),
               2:("___________",
                  "        O  ",
                  "        |  ",
                  "           ",
                  "           "),
               3:("___________",
                  "        O  ",
                  "       /|  ",
                  "           ",
                  "           "),
               4:("___________",
                  "        O  ",
                  "       /|\\ ",
                  "           ",
                  "           "),
               5:("___________",
                  "        O  ",
                  "       /|\\ ",
                  "       /   ",
                  "           "),
               6:("___________",
                  "        O  ",
                  "       /|\\ ",
                  "       / \\ ",
                  "           ")}


def display_man(wrong_guesses):
    print("********************************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("********************************")
def display_hint(hint):
    print(" ".join(hint))
    print()

def display_answer(answer):
    print()
    print(f"Correct Guess is '{" ".join(answer)}'.")
    print()

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_latters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print()
            print("Invalid input")
            continue

        if guess in guessed_latters:
            print()
            print(f"'{guess}' is already guessed")
            continue

        guessed_latters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]  == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            print()
            print("YOU WIN!")
            display_answer(answer)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses) 
            print()           
            print("YOU LOSE!")
            display_answer(answer)
            is_running = False
    print("********************************")

if __name__ == "__main__":
    main()