import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
number_of_friends = len(friends)
random_friend = random.randint(0, number_of_friends - 1)
# noinspection PyTypeHints
print(friends[random_friend])
#option 2
print(random.choice(friends))