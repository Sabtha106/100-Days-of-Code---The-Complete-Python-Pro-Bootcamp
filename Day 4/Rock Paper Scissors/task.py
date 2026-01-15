import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
list = [rock, paper, scissors]
random_choice = random.randint(0, len(list) -1)

#User choosing Rock
if random_choice == 0 and user_input == 0:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("Its a draw")
elif random_choice == 1 and user_input == 0:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You lose!")
elif random_choice == 2 and user_input == 0:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You win!")

#user choosing Paper
if random_choice == 0 and user_input == 1:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You win")
elif random_choice == 1 and user_input == 1:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("It's a Draw!")
elif random_choice == 2 and user_input == 1:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You lose!")

#user choosing Scissors
if random_choice == 0 and user_input == 2:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You lose!")
elif random_choice == 1 and user_input == 2:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("You Win!")
elif random_choice == 2 and user_input == 2:
    # noinspection PyTypeHints
    print(list[user_input])
    # noinspection PyTypeHints
    print("Computer chose:\n" +
          list[random_choice])
    print("It's a Draw!")
