#!/usr/bin/env python3
# Module 2
#   Programming Assignment 2
#     Prob-2.py

# Matt Russell

# Follow the steps below. Add your code in the blank line after each comment

# define the main function with no parameters
def main():
    # create a variable and assign it the value returned by an input function
    # that asks the user for a number. Don't forget to use the int() function.
    r = int(input("enter an number: "))
    square = r ** 2
    print("The square of ", int(r), "equals ", (square) )
    # print out a message that says: "The sqare of ? is ?" where the question
    # marks are replaced with the value read in from the user and its square.
    r = int(input("enter an number: "))
    square = r ** 2
    print("The square of ", int(r), "equals ", (square) )
 
    
    # copy your input statement from above and replace "int" with "float"
    r = float(input("enter an number: "))
    square = r ** 2
    print("The square of ", float(r), "equals ", (square) )
    
    
    # copy the print statment from above

    # copy your input statement from above and replace "int" with "eval"
    r = eval(input("enter an number: "))
    square = r ** 2
    print("The square of ", eval(r), "equals ", (square) )
    # copy the print statment from above

# call the function main
main()