#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

white_space = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input".format(white_space)

# Available options
options = ['Compound Interest', 'Simple Interest']


def main():
    print("\n")
    print("  " + decorator)
    print("{} Financial Mathematics".format(white_space))
    print("  " + decorator)
    prompt()


# Print from options and ask the user to choose one
def prompt():
    print("\n")

    for serial, option in enumerate(options, start=1):
        print("{0} {1}. {2}".format(white_space, serial, option))

    print("  " + decorator)

    try:
        choice = int(input("\n{} Enter your choice: ".format(white_space)))
    except ValueError:
        print(invalid_input)
        prompt()

    if choice in range(1, len(options) + 1):
        prompt_values(options[choice - 1])
    else:
        print(invalid_input)
        prompt()


# Prompt values for Compunt Interest or Simple Interest
def prompt_values(userChoice):
    if userChoice == 'Compound Interest':

        try:
            initial_dep = float(input("\n{} Initial deposit: ".format(white_space)))
            interest_rate = float(input("{} Annual interest rate (percent): ".format(white_space)))
            times_compded = float(input("{} Number of times the interest is compounded: ".format(white_space)))
            time = float(input("{} Number of years the money is invested for: ".format(white_space)))
        except ValueError:
            print(invalid_input)
            prompt_values(userChoice)
        except KeyboardInterrupt:
            print("\n\n{} [-] Going back to previous menu".format(white_space))
            prompt()

        result = compound_interest(initial_dep, interest_rate, times_compded, time)

    elif userChoice == 'Simple Interest':

        try:
            loan_amount = float(input("\n{} Loan amount: ".format(white_space)))
            interest_rate = float(input("{} Interest rate (percentage): ".format(white_space)))
            time = float(input("{} Duration (years): ".format(white_space)))
        except ValueError:
            print(invalid_input)
            prompt_values(userChoice)
        except KeyboardInterrupt:
            print("\n\n{} [-] Going back to previous menu".format(white_space))
            prompt()

        result = simple_interest(loan_amount, interest_rate, time)

    else:
        print(invalid_input)
        prompt_values(userChoice)

    if result != None:
        print("\n{0} Result: {1}".format(white_space, result))
    else:
        print("[-] Invalid inputs")
    prompt_values(userChoice)


# A = P(1+r/n)^nt
def compound_interest(initial_dep, interest_rate, times_compded, time):
    try:
        power = times_compded * time
        base = (1 + (((interest_rate / 100)) / times_compded))
        raised = math.pow(base, power)
        result = raised * initial_dep
        return round(result, 2)
    except ZeroDivisionError:
        return None;


# S = P * I * N
def simple_interest(loan, interestRate, time):
    return loan * (interestRate / 100) * time
