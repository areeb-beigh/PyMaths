#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

# Available identities
identities = ['sin(a + b)', 'sin(a - b)', 'cos(a + b)', 'cos(a - b)', 'tan(a + b)', 'tan(a - b)']

def main():
	print("\n")
	print("  " + decorator)
	print(whiteSpace + " Trigonometric Identities")
	print("  " + decorator)
	prompt_identity()

# Prompt the user to choose an identity, prints from the list identities
def prompt_identity():
	# We need identity as a global var to pass on to calculate() function
	global identity

	print("\n")

	for serial, identity in enumerate(identities, start=1):
		print(whiteSpace + " " + str(serial) + " " + identity)
	print("  " + decorator)

	try:
		choice = int(input('\n{} Enter your choice: '.format(whiteSpace)))
	except(ValueError):
		print(invalidInput)
		prompt_identity()


	if choice in range(1, len(identities) + 1):
		identity = identities[choice - 1]
	else:
		print(invalidInput)
		prompt_identity()

	prompt_values()

# Prompt values for a and b
def prompt_values():
	try:
		a = int(input('\n{} Enter value for a (Radians): '.format(whiteSpace)))
		b = int(input('\n{} Enter value for b (Radians): '.format(whiteSpace)))
	except(ValueError):
		print(invalidInput)
		prompt_values()
	except(KeyboardInterrupt):
		print("\n\n{} [-] Going back to previous menu".format(whiteSpace))
		prompt_identity()

	# Answer is at index 0
	result = calculate(identity, a, b)[0]

	# Formula is at index 1
	formula = calculate(identity, a, b)[1]

	print("\n{0} Formula: {1}".format(whiteSpace, formula))
	print("{0} Answer: {1}".format(whiteSpace, result))

	prompt_values()

# Do the magic, calculate the result and make the formula
def calculate(identity, a, b):
	if identity == 'sin(a + b)':
		result = (math.sin(a) * math.cos(b)) + (math.sin(b) * math.cos(a))
		formula = 'sin({0}) * cos({1}) + sin({1}) * cos({0})'.format(a, b)

	elif identity == 'sin(a - b)':
		result = (math.sin(a) * math.cos(b)) - (math.sin(b) * math.cos(a))
		formula = 'sin({0}) * cos({1}) - sin({1}) * cos({0})'.format(a, b)

	elif identity == 'cos(a + b)':
		result = (math.cos(a) * math.cos(b)) - (math.sin(a) * math.sin(b))
		formula = 'cos({0}) * cos({1}) - sin({0}) * sin({1})'.format(a, b)

	elif identity == 'cos(a - b)':
		result = (math.cos(a) * math.cos(b)) + (math.sin(b) * math.sin(a))
		formula = 'cos({0}) * cos({1}) + sin({0}) * sin({1})'.format(a, b)

	elif identity == 'tan(a + b)':
		result = (math.tan(a) + math.tan(b)) / 1 - (math.tan(a) * math.tan(b))
		formula = 'tan({0}) + tan({1}) / 1 - (tan({0}) * tan({1}))'.format(a, b)

	elif identity == 'tan(a - b)':
		result = (math.tan(a) - math.tan(b)) / 1 + (math.tan(a) * math.tan(b))
		formula = 'tan({0}) - tan({1}) / 1 + (tan({0}) * tan({1}))'.format(a, b)

	# Return the result and the formula used in a list
	return [result, formula]

	