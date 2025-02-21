#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Correctly get the last digit, ensuring it remains negative for negative numbers
lastDig = number % 10 if number >= 0 else -(-number % 10)

if lastDig == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
elif lastDig < 6:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")

