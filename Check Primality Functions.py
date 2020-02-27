"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
 You can (and should!) use your answer to Exercise 4 to help you. """


def is_prime():
    number = int(input("Enter a number: "))
    divisors = range(1, number + 1)
    newdivisors = [i for i in divisors if number % i == 0]
    if len(newdivisors) == 2:
        return str(number) + " is a prime number"
    elif number == 1:
        return str(number) + " is a prime number"
    else:
        return str(number) + " is not a prime number"


print(is_prime())
