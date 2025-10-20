#open, write, and read text file (e.g., "WordTextFile1.txt") using open(), write(), read()
#solution accepts file input to insert sentence composed of file content into text file on a new line
#solution outputs the text file contents including the new sentence
file_name = input()

with open(file_name,"r") as file:
    contents = file.read()
    sentence = " ".join(contents.split())

with open(file_name,"a") as file:
   file.write(f'\n{sentence}')
   
with open(file_name,"r") as file:
    contents = file.read()
    
print(contents)
    
"""
Lab Instructions:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.

Task:
Create a solution that accepts an input identifying the name of a text file, for example, "WordTextFile1.txt". Each text file contains three rows with one word per row. Using the open() function and write() and read() methods, interact with the input text file to write a new sentence string composed of the three existing words to the end of the file contents on a new line. Output the new file contents.

The solution output should be in the format

word1
word2
word3 
sentence
Sample Input/Output:
If the input is

WordTextFile1.txt
then the expected output is

cat
chases
dog
cat chases dog
"""
