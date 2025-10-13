user_input = input()
i = 0

while i < len(user_input):
    if (user_input[i].isalpha()):
        print(user_input[i], end = "")
    i += 1
    
print()
