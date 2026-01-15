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
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    index = 0
    for letter in chosen_word:
        if letter == guess:
            placeholder[index] = letter
            index += 1

        else:
            index += 1

    placeholder_result = "".join(placeholder)
    if placeholder_result == chosen_word:
        game_over = True
        print("You've won!")


    print(placeholder_result)





