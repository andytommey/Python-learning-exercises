"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old."""


import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
century = 100
yearsUntilCentury = century-age
x = datetime.datetime.now()
year = x.year
hundredYear = year + yearsUntilCentury

print("Hello " + name, ", You will turn 100 years old in the year", hundredYear, "that's in", yearsUntilCentury, "years time!")