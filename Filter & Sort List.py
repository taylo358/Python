''' Type your code here. '''
user_input = input()

tokens = user_input.split()

nums = []
for number in tokens:
    if int(number) >= 0:
        nums.append(int(number))

nums.sort()

print(*nums, end = " ")
    
