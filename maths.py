#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys

directory = "src"
scripts = []
white_spaces = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input\n".format(white_spaces)


def main():
    print("\n")
    print("NOTE: Use Ctrl + C (KeyboardInterrupt) to go back to any previous menu / quit application.")
    detect_scripts()
    prompt()


# Detect the scripts in 'src' and append to 'scripts'
def detect_scripts():
    global scripts
    script_list = []
    for script in os.listdir(directory):
        if script != '__init__.py' and not (os.path.isdir("src\\" + script)) and not (script.endswith('.pyc')):
            script = script.replace('.py', '').title()
            script_list.append(script)
    script_list.sort()
    scripts = script_list


# Execute a script
def execute(script):
    script = script.lower()
    imported = __import__('src.' + script, fromlist=['main'])
    try:
        imported.main()
    # This will bring you back to maths.py from the imported script
    except KeyboardInterrupt:
        print("\n\n{} [-] Going back to main menu...".format(white_spaces))
        prompt()


# Print into stuff and prompt the user for input
def prompt():
    script_number = 0
    print("\n")
    print("  " + decorator)
    print("{} PyMaths by Areeb - Main Menu".format(white_spaces))
    print("  " + decorator)
    print("\n")

    for serial, script in enumerate(scripts, start=1):
        print("{0} {1}. {2}".format(white_spaces * 2, serial, script))
        script_number += 1

    print("  " + decorator)

    try:
        choice = int(input('\n{} Enter your choice: '.format(white_spaces)))
    except ValueError:
        print(invalid_input)
        prompt()
    except KeyboardInterrupt:
        print("\n")
        print(white_spaces + " Thank you for using PyMaths! You're awesome!")
        print("\n{0} > www.areebbeigh.tk".format(white_spaces))
        sys.exit(0)

    if choice in range(1, script_number + 1):
        execute(scripts[choice - 1])
    else:
        print(invalid_input)
        prompt()


# Do the math
main()
