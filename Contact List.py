''' Type your code here. '''
contact_info = input()
contact_name = input()
contact_list = []


sorted_contact_info = contact_info.split()

for names in sorted_contact_info:
    contact_list.append(names)
    
i = 0
while i < len(contact_list):
    if contact_name in contact_list[i]:
        result = contact_list[i].replace(contact_name,'')
        result_formatted = result.replace(",","")
    i = i + 1


print(result_formatted)

