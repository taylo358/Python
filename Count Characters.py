''' Type your code here. '''
user_input = input()
items = user_input.split()
counter = 0
word_count = 1
i = 0
index = items.index(items[-1])
parameter = items[0]

while word_count <= index:
    while i < len(items[word_count]):
        if items[word_count][i] == parameter:
            counter += 1
        i += 1
    word_count += 1
    i = 0
    
    
if counter == 0:
    print(f'{counter} {parameter}\'s')
if counter == 1:
    print(f'{counter} {parameter}')
if counter > 1:
    print(f'{counter} {parameter}\'s')

