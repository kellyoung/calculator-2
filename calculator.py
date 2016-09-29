"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def calculator():
    """
    Calculates user's inputs 

    Takes in the user's inputs and directs to the operation based the operator
    used. Notifies user of invalid input.


    """
    user_input = raw_input("> ")
    while user_input != "q":
        user_input_list = user_input.split(' ')
        #check 2 inputs
        if len(user_input_list) == 2:
            operator, value1 = user_input_list
            
            #only process if value1 is type int
            try:
                value1 = int(value1)
                if operator == "square":
                    print square(value1)
                elif operator == "cube":
                    print cube(value1)
                else:
                    print "invalid input"
            except ValueError:
                print "invalid input"

        #check 3 inputs
        elif len(user_input_list) == 3:
            operator, value1, value2 = user_input_list

            #only process if value1 and value2 are type int
            try:
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
                    print "invalid input"
            except ValueError:
                print "invalid input"
        #check too many or too little inputs
        else:
            print "invalid entry"
            user_input = raw_input("> ")
            continue
        
        user_input = raw_input("> ")

calculator()