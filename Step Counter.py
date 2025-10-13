'''
A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, representing the number of feet walked, and returns an integer
that represents the number of steps walked. Then, write a main program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, 
and outputs the number of steps as an integer.
Use floating-point arithmetic to perform the conversion.
'''
# Define your function here 
import math
def feet_to_steps(user_feet):
    steps = math.floor(user_feet / 2.5)
    return round(steps)
    
if __name__ == '__main__':
    # Type your code here.
    user_feet = float(input())
    steps = feet_to_steps(user_feet)
    print(f'{steps:.0f}')
