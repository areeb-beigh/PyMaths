#!/usr/bin/python3
# -*- coding: utf-8 -*-

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

def main():
	print("\n")
	print("  " + decorator)
	print("{} Factorial".format(whiteSpace))
	print("  " + decorator)
	prompt()

# Prompt the user to enter a whole number
def prompt():
	try:
		number = int(input('\n{} Value: '.format(whiteSpace)))
		print("{0} Answer: {1}".format(whiteSpace, calculate(number)))
		prompt()
	except(ValueError):
		print(invalidInput)
		prompt()

def calculate(number):
	if number >= 1:
		result = 1
		for i in range(1, number + 1):
			result *= i
		return result
	elif number == 0:
		return 1
	else:
		raise ValueError
		