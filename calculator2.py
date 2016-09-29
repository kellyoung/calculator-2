from arithmetic2 import *


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
        
        operator = user_input_list.pop(0)
        if len(user_input_list) < 1:
            print "invalid input"
        else:
            is_all_float = True
            for index in range(len(user_input_list)):
                try:
                    user_input_list[index] = float(user_input_list[index])
                except ValueError:
                    is_all_float = False

            if is_all_float:
                if operator == "square":
                    print square(user_input_list)
                elif operator == "cube":
                    print cube(user_input_list)
                elif operator == "+" or operator == "add":
                    print add(user_input_list)
                elif operator == "-" or operator == "subtract":
                    print subtract(user_input_list)
                elif operator == "*" or operator == "multiply":
                    print multiply(user_input_list)
                elif operator == "/" or operator == "divide":
                    print divide(user_input_list)
                elif operator == "pow":
                    print power(user_input_list)
                elif operator == "%" or operator == "mod":
                    print mod(user_input_list)
                else:
                    print "invalid input"

            else:
                print "invalid entry"
                
        user_input = raw_input("> ")

calculator()