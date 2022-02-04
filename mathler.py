import random
from itertools import permutations

DIGITS = "0123456789"
OPERATORS = "+-/*"
CHARACTERS = DIGITS + OPERATORS

print("Generating equation...")
possibles = list(permutations(CHARACTERS, 6))

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

valid = list(filter(is_valid, possibles))

equations = [{
    "expression": "".join(p),
    "result": eval("".join(p))
} for p in valid]

equation = random.choice(equations)