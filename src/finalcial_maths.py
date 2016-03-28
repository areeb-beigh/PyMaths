#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

# Available options
options = ['Compound Interest', 'Simple Interest']

def main():
	print("\n")
	print("  " + decorator)
	print("{} Financial Mathematics".format(whiteSpace))
	print("  " + decorator)
	prompt()

# Print from options and ask the user to choose one
def prompt():
	print("\n")

	for serial, option in enumerate(options, start=1):
		print("{0} {1}. {2}".format(whiteSpace, serial, option))

	print("  " + decorator)

	try:
		choice = int(input("\n{} Enter your choice: ".format(whiteSpace)))
	except(ValueError):
		print(invalidInput)
		prompt()

	if choice in range(1, len(options) + 1):
		prompt_values(options[choice - 1])
	else:
		print(invalidInput)
		prompt()

# Prompt values for Compunt Interest or Simple Interest
def prompt_values(userChoice):

	if userChoice == 'Compound Interest':

		try:
			initialDeposit = float(input("\n{} Initial deposit: ".format(whiteSpace)))
			interestRate = float(input("{} Annual interest rate (percent): ".format(whiteSpace)))
			timesCompounded = float(input("{} Number of times the interest is compounded: ".format(whiteSpace)))
			time = float(input("{} Number of years the money is invested for: ".format(whiteSpace)))
		except(ValueError):
			print(invalidInput)
			prompt_values(userChoice)
		except(KeyboardInterrupt):
			print("\n\n{} [-] Going back to previous menu".format(whiteSpace))
			prompt()
		
		result = compound_interest(initialDeposit, interestRate, timesCompounded, time)

	elif userChoice == 'Simple Interest':

		try:
			loanAmount = float(input("\n{} Loan amount: ".format(whiteSpace)))
			interestRate = float(input("{} Interest rate (percentage): ".format(whiteSpace)))
			time = float(input("{} Duration: ".format(whiteSpace)))
		except(ValueError):
			print(invalidInput)
			prompt_values(userChoice)
		except(KeyboardInterrupt):
			print("\n\n{} [-] Going back to previous menu".format(whiteSpace))
			prompt()

		result = simple_interest(loanAmount, interestRate, time)

	else:
		print(invalidInput)
		prompt_values(userChoice)

	print("\n{0} Result: {1}".format(whiteSpace, result))
	prompt_values(userChoice)

# A = P(1+r/n)^nt
def compound_interest(initialDeposit, interestRate, timesCompounded, time):
	power = timesCompounded * time
	base = (1 + (( (interestRate / 100)) / timesCompounded))
	raised = math.pow(base, power)
	result = raised * initialDeposit
	return round(result,2)

# S = P * I * N
def simple_interest(loan, interestRate, time):
	return loan * (interestRate / 100) * time