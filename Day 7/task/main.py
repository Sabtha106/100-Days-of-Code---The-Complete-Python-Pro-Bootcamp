import random
<<<<<<< HEAD
import hangman_words
import hangman_art
=======
<<<<<<< HEAD
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(hangman_words.word_list)
=======
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

<<<<<<< HEAD
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(hangman_words.word_list)
=======
chosen_word = random.choice(word_list)
>>>>>>> bcafdda17d0c99f4688456720e1805602004abf8
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
<<<<<<< HEAD
print(hangman_art.logo)
print("Word to guess: " + placeholder)
=======
<<<<<<< HEAD
print(hangman_art.logo)
print("Word to guess: " + placeholder)
=======
print(placeholder)
>>>>>>> bcafdda17d0c99f4688456720e1805602004abf8
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

<<<<<<< HEAD
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

=======
<<<<<<< HEAD
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.


    display = ""
    if guess in correct_letters:
        print(f"You already guessed this letter: {guess}. Please guess again.")
=======
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a
    display = ""

>>>>>>> bcafdda17d0c99f4688456720e1805602004abf8
    for letter in chosen_word:

        if letter == guess:
            if letter in display:
                print("You have already guessed this letter!")
                print(guess)
            else:
                display += letter
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

<<<<<<< HEAD
    print("Word to guess: " + display)
=======
<<<<<<< HEAD
    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not in the word. Please guess again.")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
=======
    print(display)
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed: {guess}, you lose a live")

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

<<<<<<< HEAD
    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
=======
    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
>>>>>>> bcafdda17d0c99f4688456720e1805602004abf8
>>>>>>> a1192b920508e7a447a700dbdea950bafe88ce9a
