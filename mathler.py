#!/usr/bin/env python3

import random
from itertools import permutations

DIGITS = "0123456789"
OPERATORS = "+-/*"
CHARACTERS = DIGITS + OPERATORS

def is_valid(expression):
    if expression[0] in "+/*0-": return False # Don't start with these
    if expression[5] in OPERATORS: return False # Don't end with operator
    for n, char in enumerate(expression): 
        if char in OPERATORS: # No consecutive operators
            if n != 0 and expression[n - 1] in OPERATORS: return False
            if n != 5 and expression[n + 1] in OPERATORS: return False
        if char == "0": # No numbers starting with 0
            if n != 0 and expression[n - 1] in OPERATORS: return False
        if char == "1": # Don't multpiply by 1, don't divide by 1
            if (n == 0 or expression[n - 1] in OPERATORS): # No number before
                if (n == 5 or expression[n + 1] in OPERATORS): # number 1
                    if (n != 0 and expression[n - 1] in "*/"):
                        return False
                    if (n != 5 and expression[n + 1] == "*"):
                        return False
    result = eval("".join(expression)) # Sensible integer result
    if (10 < result < 200) and round(result) == result: return True
    return False


def make_green(char):
    return "\033[92;1m{}\033[0m".format(char)


def make_orange(char):
    return "\033[93;1m{}\033[0m".format(char)


def make_gray(char):
    return "\033[37;2m{}\033[0m".format(char)


def make_bold(char):
    return "\033[1m{}\033[0m".format(char)


def color_guess(guess, actual):
    hint = ""
    for guess_char, actual_char in zip(guess, actual):
        if guess_char == actual_char:
            hint += make_green(guess_char)
        elif guess_char in actual:
            times_green = len([
                i for i, char in enumerate(guess) if
                char == guess_char and actual[i] == guess_char
            ])
            occurences = actual.count(guess_char)
            if occurences > times_green:
                hint += make_orange(guess_char)
            else:
                 hint += make_gray(guess_char)
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


print("Find the expression that equals: {}".format(make_bold(equation["result"])))
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