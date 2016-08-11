from src import inputhandler
from src import trigonometry
from src import trigonometric_identities
from src import permutation_combination
from src import factorial

print("     Welcome to PyMaths")
options = [
    "Factorial",
    "Trigonometry",
    "Trigonometric Identities",
    "Permutation and Combination",
]

while True:
    choice = inputhandler.take_input(options, max_value=len(options))
    if choice == 1:
        factorial.get_input()
    elif choice == 2:
        trigonometry.get_input()
    elif choice == 3:
        trigonometric_identities.get_input()
    elif choice == 4:
        permutation_combination.get_input()