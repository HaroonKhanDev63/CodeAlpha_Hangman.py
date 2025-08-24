import random
import string

WORDS = ["python", "variable", "loop", "function", "module"]
MAX_INCORRECT = 6

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(WORDS)

def display_state(secret_word, guessed_letters, incorrect_guesses):
    display = " ".join([ch if ch in guessed_letters else "_" for ch in secret_word])
    print(HANGMAN_PICS[incorrect_guesses])
    print(f"Word: {display}")
    print(f"Guessed: {' '.join(sorted(guessed_letters)) if guessed_letters else '-'}")
    print(f"Attempts left: {MAX_INCORRECT - incorrect_guesses}")

def get_guess(already_guessed):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Please enter a single letter (a-z).")
            continue
        if guess in already_guessed:
            print("You already guessed that letter.")
            continue
        return guess

def play_once():
    secret_word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0

    print("\nWelcome to Hangman! Guess the word.")
    while incorrect_guesses < MAX_INCORRECT:
        display_state(secret_word, guessed_letters, incorrect_guesses)
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in secret_word:
            if all(ch in guessed_letters for ch in secret_word):
                display_state(secret_word, guessed_letters, incorrect_guesses)
                print(f"You win! The word was '{secret_word}'.")
                return
        else:
            incorrect_guesses += 1

    display_state(secret_word, guessed_letters, incorrect_guesses)
    print(f"You lost! The word was '{secret_word}'.")

def main():
    while True:
        play_once()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Hangman!")
            break

if __name__ == "__main__":
    main()
