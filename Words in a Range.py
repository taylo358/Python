# Type your code here. 
#Get name of .txt file
file_name = input()
word_1 = input()
word_2 = input()

txt_file = open(file_name)

contents = txt_file.read()

words = contents.split()

#for items in words:
#   word_list.append(words)

i = 0
#Print all words between the user inputted words (Word_1 and word_2)
while i < len(words):
    if words[i] >= word_1 and words[i] <= word_2:
        print(words[i])
    i += 1
