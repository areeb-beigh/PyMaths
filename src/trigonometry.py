#!/usr/bin/python
# -*- coding: utf-8 -*-
import math

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

# Available units
units = ['Radian', 'Degree']

# Available trig functions
functions = ['Sin', 'Cos', 'Tan', 'Cosec', 'Sec', 'Cot']

def main():
	print '\n'
	print ' ', decorator
	print whiteSpace, "Trigonometry"
	print ' ', decorator
	prompt_unit()

# Prompt for the unit
def prompt_unit():
	global unit
	print '\n'

	for serial, unit in enumerate(units, start=1):
		print "{0} {1}. {2}".format(whiteSpace, serial, unit)

	print ' ', decorator

	try:
		choice = int(raw_input('\n{} Enter your choice: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt_unit()

	if choice in range(1, len(units) + 1):
		unit = units[choice - 1]
		prompt_function()
	else:
		print invalidInput
		prompt_unit()

# Prompt for the trig funcntion
def prompt_function():
	global function
	print '\n'

	for serial, function in enumerate(functions, start=1):
		print "{0} {1}. {2}".format(whiteSpace, serial, function)

	print ' ', decorator

	try:
		choice = int(raw_input('\n{} Enter your choice: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt_function()
	except KeyboardInterrupt:
		print '\n\n{} [-] Going back to unit choice...'.format(whiteSpace)
		prompt_unit()

	if choice in range(1, len(functions) + 1):
		function = functions[choice - 1]
		prompt_value()
	else:
		print invalidInput
		prompt_function()

# Prompt value (degree / radian)
def prompt_value():
	try:
		value = float(raw_input('\n{} Angle: '.format(whiteSpace)))
	except KeyboardInterrupt:
		print '\n\n{} [-] Going back to function choice...'.format(whiteSpace)
		prompt_function()
	except ValueError:
		print invalidInput
		prompt_value()

	answer = calculate(unit, function, value)
	print '{0} Answer: {1}'.format(whiteSpace, answer)

	prompt_value()

# Do the magic
def calculate(unit, function, value):
	def sin(value):
		return math.sin(value)
	def cos(value):
		return math.cos(value)
	def tan(value):
		return math.tan(value)
	def cosec(value):
		return 1 / sin(value)
	def sec(value):
		return 1 / cos(value)
	def cot(value):
		return 1 / tan(value)

	if function == 'Sin':

		# If chosen unit was Radian
		if unit == 'Radian':
			return sin(value)

		# If chosen unit was Degree
		elif unit == 'Degree':
			return sin(round(math.radians(value), 2))

	elif function == 'Cos':

		if unit == 'Radian':
			return cos(value)

		elif unit == 'Degree':
			return cos(round(math.radians(value), 2))

	elif function == 'Tan':

		if unit == 'Radian':
			return tan(value)

		elif unit == 'Degree':
			return tan(round(math.radians(value), 2))

	elif function == 'Cosec':

		if unit == 'Radian':
			return cosec(value)

		elif unit == 'Degree':
			return cosec(round(math.radians(value), 2))

	elif function == 'Sec':

		if unit == 'Radian':
			return sec(value)

		elif unit == 'Degree':
			return sec(round(math.radians(value), 2))

	elif function == 'Cot':

		if unit == 'Radian':
			return cot(value)

		elif unit == 'Degree':
			return cot(round(math.radians(value), 2))
			
	else:
		return "[-] Unexpected error occured"