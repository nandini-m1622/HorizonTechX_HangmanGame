import random

# List of predefined words
words = ["python", "computer", "student", "program", "college"]

# Select a random word
word = random.choice(words)

# Create blanks for the guessed word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum wrong attempts
attempts = 6

print("===================================")
print("       WELCOME TO HANGMAN")
print("===================================")
print("Guess the word one letter at a time.")
print("You have", attempts, "incorrect guesses.\n")

# Game loop
while attempts > 0 and "_" in guessed_word:

    print("Word:", " ".join(guessed_word))
    print("Wrong Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check valid input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    # Check repeated letter
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if letter is in the word
    if guess in word:
        print("Correct Guess!\n")

        # Reveal all matching letters
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess!\n")

# Result
if "_" not in guessed_word:
    print("Congratulations!")
    print("You guessed the word:", word)
else:
    print("Game Over!")
    print("The correct word was:", word)