#!/usr/bin/python
# -*- coding: utf-8 -*-
from factorial import calculate as factorial

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

def main():
	print '\n'
	print ' ', decorator
	print "{} Permutations & Combinations".format(whiteSpace)
	print ' ', decorator
	prompt()

# Prompt for values for n and r
def prompt():
	try:
		n = int(raw_input('\n{} Value of n: '.format(whiteSpace)))
		r = int(raw_input('{} Value for r: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt()
	
	result = calculate(n, r)
	print '\n'
	print '{0} Permutations: {1}'.format(whiteSpace, result[0])
	print '{0} Combinations: {1}'.format(whiteSpace, result[1])
	prompt()

# Do the calculations
def calculate(n, r):
	try:
		permutation = factorial(n) / factorial(n - r)
		combination = factorial(n) / (factorial(r) * factorial(n - r))
	# This error comes from factioral()
	except ValueError:
		permutation = 0
		combination = 0

	# Return the number of permutations and combinations in a list
	return [permutation, combination]