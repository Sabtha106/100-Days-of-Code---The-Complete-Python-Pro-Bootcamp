from tkinter import Variable

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#to do: work how much they need to pay based on their size choice.
bill = 0

if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2

elif size == "M":
    bill += 20
    if pepperoni == "Y":
        bill += 3

elif size == "L":
    bill += 25
    if pepperoni == "Y":
        bill += 3
elif extra_cheese == "Y":
    bill += 1
print(f"Final bill is: R{bill}")
#TO DO: work out how much to add to their bill based on their pepperoni choice.

