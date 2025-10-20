import csv

filename = input()

with open(filename, "r") as file:
    reader = csv.reader(file)
    row = list(reader)
    stripped_row1 = [item.strip() for item in row [0]]
    stripped_row2 = [item.strip() for item in row [1]]
    
def convert(a):
    it = iter(a)
    dct = dict(zip(it,it))
    return dct
    
print(convert(stripped_row1))
print(convert(stripped_row2))

#test = convert(stripped_row1)
#print(stripped_row1.index("b"))
#print(test.keys())

#print(help(list.index))

"""
Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.

The solution output should be in the format

{'key': 'value', 'key': 'value', 'key': 'value'}
{'key': 'value', 'key': 'value', 'key': 'value'}
Sample Input/Output:
If the input is

input1.csv
then the expected output is

{'a': '100', 'b': '200', 'c': '300'}
{'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}
Alternatively, if the input is

input2.csv
then the expected output is

{'d': '400', 'e': '500', 'f': '600'}
{'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}
"""
