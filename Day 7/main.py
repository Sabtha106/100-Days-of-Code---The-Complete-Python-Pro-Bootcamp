import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = []
for blank in chosen_word:
    placeholder.append("_")
placeholder_result = "".join(placeholder)
print(placeholder_result)

# TODO-1: - Use a while loop to let the user guess again.
while placeholder_result != chosen_word:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    display = []
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"

    letter_index = ""
    for letter in chosen_word:
        if letter == guess:
            letter_index = chosen_word.index(letter)
            placeholder[letter_index] = letter

    placeholder_result = "".join(placeholder)
    print(placeholder_result)

