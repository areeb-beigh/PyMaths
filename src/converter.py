#!/usr/bin/python3
# -*- coding: utf-8 -*-
from units import unit
from units.predefined import define_units

define_units()

white_space = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input".format(white_space)

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
    print("\n")
    print("  " + decorator)
    print("{} Converter".format(white_space))
    print("  " + decorator)
    assign_units()
    prompt_conversion()


# Assign units using unit() to the units of each quantity in 'conversions'
def assign_units():
    for measure_type in conversions:
        measure_type = measure_type.lower()
        dictionary = {}

        for si_unit, abbrv in eval(measure_type):
            si_unit = si_unit.lower()
            assignUnit = 'unit(\'{}\')'.format(abbrv)
            pair = {si_unit: assignUnit}
            dictionary.update(pair)

        measure_type += '_dict'
        eval(measure_type).update(dictionary)


# Asks the user to select the type of quantity he wants to convert from 'conversions'
def prompt_conversion():
    global conversion_name, conversion_type
    print("\n")

    conversions.sort()

    for serial, conversion in enumerate(conversions, start=1):
        print("{0} {1}. {2}".format(white_space, serial, conversion))

    print("  " + decorator)

    try:
        choice = int(input('\n{} Enter your choice: '.format(white_space)))
    except(ValueError):
        print(invalid_input)
        prompt_conversion()

    if choice in range(1, len(conversions) + 1):
        conversion_name = conversions[choice - 1].lower()
        conversion_type = eval(conversions[choice - 1].lower())
        prompt_unit(conversion_type)
    else:
        print(invalid_input)
        prompt_conversion()

    # Asks the user for the unit of the value he wants to input


def prompt_unit(conversion_type):
    print("\n")

    for serial, (unit, abbrv) in enumerate(conversion_type, start=1):
        print("{0} {1}. {2} - {3}".format(white_space, serial, unit, abbrv))

    print("  " + decorator)

    try:
        choice = int(input('\n{} Enter your choice: '.format(white_space)))
    except ValueError:
        print(invalid_input)
        prompt_unit(conversion_type)
    except KeyboardInterrupt:
        print("\n\n{} [-] Going back to conversion choice...".format(white_space))
        prompt_conversion()

    if choice in range(1, len(conversion_type) + 1):
        unit = conversion_type[choice - 1][1]
        ask_input(unit)
    else:
        print(invalid_input)
        prompt_unit(conversion_type)


# Asks the user the value to convert
def ask_input(given_unit):
    try:
        value = float(input('\n{0} Enter the value in {1}: '.format(white_space, given_unit)))
    except ValueError:
        print(invalid_input)
        ask_input(given_unit)
    except KeyboardInterrupt:
        print("\n\n{} [-] Going back to unit choice...".format(white_space))
        prompt_unit(conversion_type)

    results = calculate(conversion_name, value, given_unit)
    print("\n")
    print("{} Conversions: ".format(white_space))
    print("\n")
    for result in results:
        print("{0} {1} {2} = {3}".format(white_space, value, unit(given_unit), result))
    print("  " + decorator)

    ask_input(given_unit)


# Does the conversion
# name = length, value = given value, given unit = unit which user chose in prompt_unit()
def calculate(name, value, givenUnit):
    conversion_dict = eval(name + '_dict')
    results = []
    for newUnit in conversion_dict.values():
        converted_value = eval(newUnit)(unit(givenUnit)(value))
        results.append(converted_value)

    return results
