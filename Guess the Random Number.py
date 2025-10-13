# TODO: Import the random module
import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    random_number = random.randint(1, 100)
    if num == random_number:
        print(f'{num} is correct!')
    if num > random_number:
        print(f'{num} is too high. Random number was {random_number}.')
    if num < random_number:
        print(f'{num} is too low. Random number was {random_number}.')
    # TODO: Compare parameter num to the random number
    return random_number
    
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for item in tokens:
        # Convert the string tokens into integers
        num = int(item)
        number_guess(num)
