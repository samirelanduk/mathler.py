#!/usr/bin/env python3

import random
from itertools import permutations

DIGITS = "0123456789"
OPERATORS = "+-/*"
CHARACTERS = DIGITS + OPERATORS

def is_valid(expression):
    if expression[0] in "+/*0": return False # Don't start with these
    if expression[5] in OPERATORS: return False # Don't end with operator
    for n, char in enumerate(expression): # No consecutive operators
        if char in OPERATORS:
            if n != 0 and expression[n - 1] in OPERATORS: return False
            if n != 5 and expression[n + 1] in OPERATORS: return False
        if char == "0": # Numbers starting with 0
            if n != 0 and expression[n - 1] in OPERATORS: return False
    result = eval("".join(expression)) # Sensible integer result
    if (0 < result < 200) and round(result) == result: return True
    return False


def make_green(char):
    return "\033[92;1m{}\033[0m".format(char)


def make_orange(char):
    return "\033[93;1m{}\033[0m".format(char)


def make_gray(char):
    return "\033[37;2m{}\033[0m".format(char)


def color_guess(guess, actual):
    hint = ""
    for guess_char, actual_char in zip(guess, actual):
        if guess_char == actual_char:
            hint += make_green(guess_char)
        elif guess_char in actual:
            hint += make_orange(guess_char)
        else:
            hint += make_gray(guess_char)
    return hint

print()
print("Generating equation...")
possibles = permutations(CHARACTERS, 6)
valid = filter(is_valid, possibles)
equations = [{
    "expression": "".join(p), "result": eval("".join(p))
} for p in valid]
equation = random.choice(equations)


print("Find the expression that equals: " + str(int(equation["result"])))
print()
guess_number = 1
while True:
    guess = input("Guess {}: ".format(guess_number))
    if len(guess) != 6:
        print("Equation must have six characters")
    elif not is_valid(guess):
        print("Not a valid guess")
    elif eval(guess) != equation["result"]:
        print("That doesn't equal {}".format(equation["result"]))
    elif guess != equation["expression"]:
        print(color_guess(guess, equation["expression"]))
        print()
        guess_number += 1
        if guess_number > 6:
            print("It was {}".format(equation["expression"]))
            break
    else:
        print(color_guess(guess, equation["expression"]))
        print("Yes!")
        break
print()