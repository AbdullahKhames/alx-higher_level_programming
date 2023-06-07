#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tok = "Last digit of"
num_str = str(number)
assert isinstance(number, (int, float)), "TypeError"
last_digit = int(num_str[-1])

if number < 0:
    last_digit = -last_digit

if last_digit == 0:
    print(f"{tok} {number} is {last_digit} and is 0")
elif (last_digit < 6) and last_digit != 0:
    print(f"{tok} {number} is {last_digit} and is less than 6 and not 0")
elif (last_digit > 5):
    print(f"{tok} {number} is {last_digit} and is greater than 5")
