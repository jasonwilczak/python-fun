# sample.py

# allows you to parse command line arguments (the 'name' input in this case)
import argparse
# allows you to use math functions (use cmath for comnplex numbers)
import math

# function that takes in a name and prints a greeting
# there are lots of ways to handle arguments, you can find more info here: https://www.w3schools.com/python/python_functions.asp 
# make sure do defensive coding in your function, check if number, numnber boundaries, etc
def greet(name, age):
    print(f"Hello, {name}!")
    if (math.isnan(age)): print(f"You didn't enter a valid age")
    else: print(f"You are {age} years old")

# if you want to add more math functions, you can find them here: https://docs.python.org/3/library/math.html 

# this validates you are runninpytg from the command line and not part of sonme other execution
# if you want to modify the add_argument, you can find more here: https://docs.python.org/3/library/argparse.html 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet someone")
    parser.add_argument("name", type=str, help="The name of the person to greet")
    parser.add_argument("age", type=int, help="The age of the person to greet")
    args = parser.parse_args()
    greet(args.name,args.age)