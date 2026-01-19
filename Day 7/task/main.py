import random
from operator import index

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

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = []
correct_letters = []
for position in chosen_word:
    placeholder += "_"
    correct_letters += "_"

placeholder_result = "".join(placeholder)
correct_letters_result = "".join(correct_letters)
print(placeholder_result)

game_over = False
lives = 6
while not game_over and lives > 0:
    guess = input("Guess a letter: ").lower()

    index = 0
    display = ""
    for letter in chosen_word:
        if letter == guess:
            correct_letters[index] = letter
            display += letter
            index += 1
        else:
            display += "_"
            index += 1

    correct_letters_result = "".join(correct_letters)
    print(correct_letters_result)

    # TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if display == placeholder_result:
        lives -= 1
        ascii_live = stages[lives]
        print(ascii_live)


        if lives == 0:
            print("You lost.")
            game_over = True
    # TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.
    elif display != placeholder_result:
        ascii_live = stages[lives]
        print(ascii_live)
        if correct_letters_result == chosen_word:
            game_over = True
            print("You win!")





