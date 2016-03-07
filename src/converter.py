#!/usr/bin/python
# -*- coding: utf-8 -*-
from units import unit
from units.predefined import define_units

define_units()

whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input".format(whiteSpace)

# Defining some types of measurement with their units in lists
conversions = ['Length', 'Weight', 'Volume', 'Time', 'Computer']

length = [('Millimeters', 'mm'), ('Centimeters', 'cm'),
			('Decimeters', 'dm'), ('Meters', 'm'),
			('Kilometers', 'km'), ('Inches', 'inch'),
			('Feet', 'ft'), ('Yards', 'yd'),
			('Fathoms', 'fathom'), ('Rods', 'rd'),
			('Furlong', 'fur'), ('Leagues', 'league'),
			('Miles', 'mi'), ('Nautical Miles', 'NM'),
			('Cables', 'cable'), ('Lighth Years', 'ly'),
			('Astronomical Units', 'AU'), ('Parsec', 'pc')
			]

weight = [('Miligrams', 'mg'), ('Centigrams', 'cg'), 
			('Decigrams', 'dg'), ('Grams', 'g'), 
			('Kilograms', 'kg'), ('Ounces', 'oz'),
			('Pounds', 'lb'), ('Tons', 'ton'),
			('Metric Ton', 'tonne'), ('Grains', 'grain'), 
			('Drams', 'dr'), ('Hundredweight (Quintal)', 'cwt')
			]

volume = [('Milliliter', 'mL'), ('Centiliter', 'cL'), 
			('Deciliter', 'dL'), ('Liter', 'L'),
			('Kiloliter', 'kL')]

time = [('Second', 's'), ('Minute', 'min'),
			('Hour', 'h'), ('Day', 'day'),
			('Week', 'wk')]

computer = [('Bit', 'B'), ('Kibibyte', 'KiB'), 
				('Mebibyte', 'MiB'), ('Gegibyte', 'GiB'),
				('Tebibyte', 'TiB'), ('Pecibyte', 'PiB')
				]

# These dictionaries will be filled by assign_units()
length_dict = {}
weight_dict = {}
volume_dict = {}
time_dict = {}
computer_dict = {}

'''
Here's what a dict looks like after assign_units():

computer_dict:

[('Bit', 'B'), ('Kibibyte', 'KiB'), ('Mebibyte', 'MiB'), 
('Gegibyte', 'GiB'), ('Tebibyte', 'TiB'), ('Pecibyte', 'PiB')]
'''

def main():
	print '\n'
	print ' ', decorator
	print "{} Converter".format(whiteSpace)
	print ' ', decorator
	assign_units()
	prompt_conversion()

# Assign units using unit() to the units of each quantity in 'conversions'
def assign_units():
	for measureType in conversions:
		measureType = measureType.lower()
		dictionary = {}

		for siUnit, abbrv in eval(measureType):
			siUnit = siUnit.lower()
			assignUnit = 'unit(\'{}\')'.format(abbrv)
			pair = {siUnit: assignUnit}
			dictionary.update(pair)
	
		measureType += '_dict'
		eval(measureType).update(dictionary)

# Asks the user to select the type of quantity he wants to convert from 'conversions'
def prompt_conversion():
	global conversionName, conversionType
	print '\n'

	conversions.sort()

	for serial, conversion in enumerate(conversions, start=1):
		print "{0} {1}. {2}".format(whiteSpace, serial, conversion)
	
	print ' ', decorator

	try:
		choice = int(raw_input('\n{} Enter your choice: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt_conversion()
	
	if choice in range(1, len(conversions) + 1):
		conversionName = conversions[choice - 1].lower()
		conversionType = eval(conversions[choice - 1].lower())
		prompt_unit(conversionType)
	else:
		print invalidInput
		prompt_conversion() 

# Asks the user for the unit of the value he wants to input
def prompt_unit(conversionType):
	print '\n'

	for serial, (unit, abbrv) in enumerate(conversionType, start=1):
		print "{0} {1}. {2} - {3}".format(whiteSpace, serial, unit, abbrv)

	print ' ', decorator

	try:
		choice = int(raw_input('\n{} Enter your choice: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt_unit(conversionType)
	except KeyboardInterrupt:
		print '\n\n{} [-] Going back to conversion choice...'.format(whiteSpace)
		prompt_conversion()

	if choice in range(1, len(conversionType) + 1):
		unit = conversionType[choice - 1][1]
		ask_input(unit)
	else:
		print invalidInput
		prompt_unit(conversionType)

# Asks the user the value to convert
def ask_input(givenUnit):
	try:
		value = float(raw_input('\n{0} Enter the value in {1}: '.format(whiteSpace, givenUnit)))
	except ValueError:
		print invalidInput
		ask_input(givenUnit)
	except KeyboardInterrupt:
		print '\n\n{} [-] Going back to unit choice...'.format(whiteSpace)
		prompt_unit(conversionType)

	results = calculate(conversionName, value, givenUnit)
	print '\n'
	print "{} Conversions: ".format(whiteSpace)
	print '\n'
	for result in results:
		print "{0} {1} {2} = {3}".format(whiteSpace, value, unit(givenUnit), result)
	print ' ', decorator

	ask_input(givenUnit)

# Does the conversion
# name = length, value = given value, given unit = unit which user chose in prompt_unit()
def calculate(name, value, givenUnit):
	conversionDict = eval(name + '_dict')
	results = []
	for newUnit in conversionDict.values():
		convertedValue = eval(newUnit)(unit(givenUnit)(value))
		results.append(convertedValue)

	return results