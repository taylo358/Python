names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

# Type your code here.
try:
    print(f'Name: {names[index]}')
except IndexError:
    if index < 0:
        print("Exception! list index out of range")
        print(f'The closest name is: {names[0]}')
    if index > 0:
        print("Exception! list index out of range")
        print(f'The closest name is: {names[-1]}')
