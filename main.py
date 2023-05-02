import random
import requests
import hangman_stages

# print(hangman_stages.add_left_leg)

# IMPORTANT
# TODO: when pushing to GitHub, recieve error regarding RSA key. Rectify

def main():

    attempts = 0

    while attempts < 7:
    # TODO: If 
        letters_guessed = []

        correct_word = get_word()
        
        secret_word = "".join("_" for _ in correct_word)
        print("Hello World")

        attempts += 1
        print(attempts)


    
        ask_for_new_game = input("New game (y/n)? ").lower()
        print(ask_for_new_game)
        if ask_for_new_game == "n":
            break
        elif ask_for_new_game == "y":
            main()
        else:
            print("Please type either y or n")


def new_game():
    new_game = False
    while new_game == False:
        ask_for_new_game = input("New game (y/n)? ").lower()
        print(ask_for_new_game)
        if ask_for_new_game == "n":
            break
        elif ask_for_new_game == "y":
            main()
        else:
            print("Please type either y or n")

def game_lost():
    print("Sorry, you lost!")

def game_won():
    print("Congratulations, you won!")


def get_word():
    url = "https://free-random-word-generator-api.p.rapidapi.com/random-word"

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "0c8d46ec9dmsh80eb5c0f8fc1fbcp12b8fejsn1f6d4e268310",
        "X-RapidAPI-Host": "free-random-word-generator-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def determine_stage():
    """"""
    wrong_guess_amount = 0


if __name__ == "__main__":
    main()
