#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig=number%10
if(lastDig <6):
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0.")
elif(lastDig == 0):
    print(f"Last digit of {number} is {lastDig} and is not 0.")
elif(lastDig > 5) :
    print(f"Last digit of {number} is {lastDig} and is greater than 5.")
