#!/usr/bin/env python3
# Module 2
#   Programming Assignment 2
#     Prob-3.py

# Matt Russell

def example():
    print("\nExample Output")

    # print a blank line
    print()

    # create three variables and assign three values in a single statement
    v1, v2, v3 = 21, 12.34, "hello"

    # print the variables
    print("v1:", v1)
    print("v2:", v2)
    print("v3:", v3)


def studentCode():
    # replace <name> with your name
    print("\nMatt's Output")
    
    # print a blank line
    print()

    # replicate the assignment statement above, but use your own variable
    # names and values
    var1, var2, var3 = 10, 2.87, "Que hora es?"
    # print the values of the 3 variables
    print("var1:", var1)
    print("var2:", var2)
    print("var3:", var3)
    # Get 3 values from the user and assign them to the variables defined
    # above. See the page in Canvas on Simulataneous Assignment
    # BONUS POINTS for using the split() method
    print()
    print()
    print("Enter 3 numbers ")
    var1 = (input("1st number: "))
    var2 = (input("2nd number: "))
    var3 = (input("3rd number: "))
    print("var1:", var1)
    print("var2:", var2) 
    print("var3:", var3)
   
    print()
    a, b, c = input("enter 3 numbers between 0 and 9: ")

    print("var1=",a, "var2=", b , "var3=", c)

example()
studentCode()

