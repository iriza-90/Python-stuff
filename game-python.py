import random

def game():
    words = ["apple", "banana", "cherry", "grape", "orange"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 5

    print("Welcome to Hangman!")
    while incorrect_guesses < max_attempts:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "
        print(display_word)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                print("Correct!")
            else:
                incorrect_guesses += 1
                print(f"Wrong guess! You have {max_attempts - incorrect_guesses} attempts left.")

        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break

    if "_" in display_word:
        print(f"Sorry, you're out of attempts. The word was: {secret_word}")

hangman()
