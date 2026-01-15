#capture a number from user input
#convet it into integer
user_number = int(input("Type a number\n"))
#check if the number is even or odd number using modulo operator and condition statement
if user_number % 2 == 0:
    print("even")
else:
    print("Odd")