"""Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

number = input("Enter a number: ")

if int(number) % 4 == 0:
    print("Your number is even and is also a multiple of 4")
elif int(number) % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")

num = input("Enter a number to check: ")
check = input("Enter a number to divide by: ")

if int(num) % int(check) == 0:
    print(check + " divides equally into " + num)
else:
    print(check + " does not divide equally into " + num)
