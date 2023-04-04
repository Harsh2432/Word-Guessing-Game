import random

# List of words to choose from
words = ["apple", "banana", "cherry", "orange", "pear", "peach", "plum"]

# Choose a random word from the list
word = random.choice(words)

# Convert the word to a list of letters
letters = list(word)

# Create a list of underscores the same length as the word
underscores = ["_"] * len(word)

# Keep track of the number of incorrect guesses
incorrect_guesses = 0

# Keep track of the letters that have already been guessed
guessed_letters = []

# Game loop
while True:
    # Print the current state of the word
    print(" ".join(underscores))
    
    # Ask the player to guess a letter
    guess = input("\nGuess a letter: ").lower()
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("\nYou already guessed that letter.")
        continue
        
    # Add the guess to the list of guessed letters
    guessed_letters.append(guess)
    
    # Check if the guess is correct
    if guess in letters:
        # Update the underscores with the guessed letter
        for i in range(len(word)):
            if letters[i] == guess:
                underscores[i] = guess
        # Check if the player has guessed all the letters
        if "_" not in underscores:
            print("\nCongratulations, you guessed the word!")
            break
    else:
        print("\nSorry, that letter is not in the word.")
        incorrect_guesses += 1
        # Check if the player has used up all their guesses
        if incorrect_guesses == 6:
            print("\nSorry, you ran out of guesses. The word was", word)
            break
