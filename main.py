import os
import random
import requests
import dotenv
import hangman_stages

def main():

    attempts = 0

    correct_word = get_word()
    print(correct_word)
    
    letters_guessed = []
    #secret_word = "".join("_" for letter in correct_word if letter not in letters_guessed)
    secret_word = ["_"] * len(correct_word)


    while attempts < 7:
        
        print(attempts)

        guess = input("Guess a letter: ")

        for i, letter in enumerate(correct_word):
            # Check if current looped letter is equal to the guess
            if letter != "_" and guess == letter:
                # Set the underscore at the position to the correct letter
                secret_word[i] = letter
        
        print(f"Secret word: {''.join(secret_word)}")

    

        #print(secret_word)

        # if secret word has been correctly guessed
        if "_" not in secret_word:
            print("You won")
            break

        if len(guess) > 1 or guess in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            print("Please only input a single letter / No numbers.")
            continue

        if guess in letters_guessed:
            print("You have already guessed that letter. Try again.")
        else:
            letters_guessed.append(guess)

        if guess in correct_word:
            print("That letter is correct")
        else:
            attempts += 1
            print("Incorrect")
        
        # TODO: If player lost game



    keep_playing = True
    while keep_playing == True:
        
        ask_for_new_game = input("New game (y/n)? ").lower()
        if ask_for_new_game == "n":
            print("Thanks for playing :)")
            keep_playing = False
            break
        elif ask_for_new_game == "y":
            main()
        else:
            print("Please type either y or n")
            continue



def get_word():
    dotenv.load_dotenv()

    API_KEY = os.getenv("API_KEY")

    url = "https://free-random-word-generator-api.p.rapidapi.com/random-word"

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "free-random-word-generator-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()

def determine_stage():
    """"""
    wrong_guess_amount = 0



if __name__ == "__main__":
    main()
