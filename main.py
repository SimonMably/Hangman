import random
import requests
import hangman_stages

# print(hangman_stages.add_left_leg)

def main():

    attempts = 0

    correct_word = get_word()
    secret_word = "".join("_" for _ in correct_word)

    letters_guessed = []

    while attempts < 7:
    
        print(attempts)


        guess = input("Guess a letter: ").lower()
        if guess in letters_guessed:
            print("You have already guessed that letter. Try again.")
        else:
            letters_guessed.append(guess)


        if guess in correct_word:
            print("That letter is correct")
        else:
            attempts += 1
            print("Incorrect")




    ############################################################################
    ask_for_new_game = input("New game (y/n)? ").lower()
    print(ask_for_new_game)
    if ask_for_new_game == "n":
        print("Thanks for playing :)")
    if ask_for_new_game == "y":
        main()
    else:
        print("Please type either y or n")




def game_lost():
    print("Sorry, you lost!")

def game_won():
    print("Congratulations, you won!")

# TODO: get word here

def determine_stage():
    """"""
    wrong_guess_amount = 0

def determine_correct_guess(guessed_letter):
    pass


if __name__ == "__main__":
    main()
