import os
import requests
import dotenv
import hangman_stages

def main():
    """Game loop."""

    attempts = 0

    correct_word = get_word()
    
    letters_guessed = []
    
    secret_word = ["_"] * len(correct_word)


    while attempts != 6:
        if attempts == 0 and len(letters_guessed) == 0:
            print("".join(secret_word))

        print(determine_stage(attempts))
        # print(attempts)

        guess = input("\nGuess a letter: ")

        for i, letter in enumerate(correct_word):
            # Check if current looped letter is equal to the guess
            if letter != "_" and guess == letter:
                # Set the underscore at the position to the correct letter
                secret_word[i] = letter
        
        print(f"\n{''.join(secret_word)}\n")

        # if secret word has been correctly guessed
        if "_" not in secret_word:
            print("\nCongratulations!! You won!")
            break

        if len(guess) > 1 or guess in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            print("Invalid guess. Please only input a single letter / No numbers.")
            continue

        if guess == "" or guess == " ":
            print("Invalid guess. Guesses must contain a letter.")
            continue

        if guess in letters_guessed:
            print("You have already guessed that letter. Try again.")
            continue
        else:
            letters_guessed.append(guess)

        if guess in correct_word:
            print("\nThat letter is correct")
        else:
            attempts += 1
            print("\nIncorrect")
        
        if attempts == 6:
            print(determine_stage(attempts))
            print(f"\nYou lost!! The correct word is {correct_word}")

    keep_playing = True
    while keep_playing == True:
        
        ask_for_new_game = input("\nNew game (y/n)? ").lower()
        if ask_for_new_game == "n":
            print("\nThanks for playing :)")
            keep_playing = False
            break
        elif ask_for_new_game == "y":
            clear_screen()
            main()
        else:
            print("\nPlease type either y or n")
            continue

def get_word():
    """Retrieves a random word via Free Random Word Generator API hosted on RapidAPI. Returns response.json().
    
    API url: https://free-random-word-generator-api.p.rapidapi.com/random-word
    """
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

def determine_stage(attempt: int):
    """Determine which hangman image to show, depending on incorrect attempts to guess the word. Returns stage depending on failed attempt amount."""
    if attempt == 0:
        return hangman_stages.empty_gallows
    elif attempt == 1:
        return hangman_stages.add_head
    elif attempt == 2:
        return hangman_stages.add_torso
    elif attempt == 3:
        return hangman_stages.add_left_arm
    elif attempt == 4:
        return hangman_stages.add_right_arm
    elif attempt == 5:
        return hangman_stages.add_right_leg
    elif attempt == 6:
        return hangman_stages.add_left_leg

def clear_screen():
    """Clears terminal screen. Works for Window (tested and works). Also account for Linux and Mac OS, but not tested"""
    # For windows
    if os.name == "nt":
        _ = os.system("cls")
    else:
        # For Linux / Mac OS
        _ = os.system("clear")


if __name__ == "__main__":
    main()
