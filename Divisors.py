"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""


number = int(input("Enter a number: "))
divisors = range(1, number + 1)
newDivisors = [i for i in divisors if number % i == 0]

print(newDivisors)

if len(newDivisors) == 2:
    print(str(number) + " is a prime number")
elif number == 1:
    print(str(number) + " is a prime number")
else:
    print(str(number) + " is not a prime number")
