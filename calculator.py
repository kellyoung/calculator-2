"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator():
    user_input = raw_input("> ")
    while user_input != "q":
        user_input_list = user_input.split(' ')
        if len(user_input_list) == 2:
            operator, value1 = user_input_list

        elif len(user_input_list) == 3:
            operator, value1, value2 = user_input_list
            value1 = int(value1)
            value2 = int(value2)

            if operator == "+" or operator == "add":
                print add(value1, value2)
            elif operator == "-" or operator == "subtract":
                print subtract(value1, value2)
            elif operator == "*" or operator == "multiply":
                print multiply(value1, value2)
            elif operator == "/" or operator == "divide":
                print divide(value1, value2)
            elif operator == "pow":
                print power(value1, value2)
            elif operator == "%" or operator == "mod":
                print mod(value1, value2)

        else:
            print "invalid entry"
            user_input = raw_input("> ")
            continue
        
        user_input = raw_input("> ")

calculator()