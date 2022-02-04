from itertools import permutations

DIGITS = "0123456789"
OPERATORS = "+-/*"
CHARACTERS = DIGITS + OPERATORS

print("Generating equation...")
possibles = list(permutations(CHARACTERS, 6))