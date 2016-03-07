#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

directory = "src"
scripts = []
whiteSpace = "   "
decorator = "-" * 35
invalidInput = "\n{} [-] Invalid input\n".format(whiteSpace)

def main():
	print '\n'
	print "NOTE: Use Ctrl + C (KeyboardInterrupt) to go back to any previous menu / quit application."
	detect_scripts()
	prompt()

# Detect the scripts in 'src' and append to 'scripts'
def detect_scripts():
	global scripts
	scriptList = []
	for script in os.listdir(directory):
		if script != '__init__.py' and not(script.endswith('.pyc')):
			script = script.replace('.py', '').title()
			scriptList.append(script)
	scriptList.sort()
	scripts = scriptList

# Execute a script
def execute(script):
	script = script.lower()
	imported = __import__('src.' + script, fromlist = ['main'])
	try:
		imported.main()
	# This will bring you back to maths.py from the imported script
	except KeyboardInterrupt:
		print "\n\n{} [-] Going back to main menu...".format(whiteSpace)
		prompt()

# Print into stuff and prompt the user for input
def prompt():
	scriptsNumber = 0
	print '\n'
	print ' ', decorator
	print "{} PyMaths by Areeb - Main Menu".format(whiteSpace)
	print ' ', decorator
	print '\n'

	for serial, script in enumerate(scripts, start=1):
		print '{0} {1}. {2}'.format(whiteSpace * 2, serial, script)
		scriptsNumber += 1

	print ' ', decorator

	try:
		choice = int(raw_input('\n{} Enter your choice: '.format(whiteSpace)))
	except ValueError:
		print invalidInput
		prompt()
	except KeyboardInterrupt:
		print "\n"
		print whiteSpace, "Thank you for using PyMaths! You're awesome!"
		print "\n{0} > www.areebbeigh.tk".format(whiteSpace)
		sys.exit(0)

	if choice in range(1, scriptsNumber + 1):
		execute(scripts[choice - 1])
	else:
		print invalidInput
		prompt()

# Do the math
main()