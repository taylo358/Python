''' Type your code here. '''
total_change = int(input())

dollars = total_change // 100
quarters = (total_change - (dollars * 100)) // 25
dimes = (total_change - (dollars * 100) - (quarters * 25)) // 10
nickels = ((total_change - (dollars * 100)) - (quarters * 25) - (dimes * 10)) // 5
pennies = (total_change - (dollars * 100)) - (quarters * 25) - (dimes * 10) - (nickels * 5)

if total_change <= 0:
    print("No change")
    
if dollars == 1:    
    print(f'{dollars} Dollar')
if dollars > 1:
    print(f'{dollars} Dollars')
if quarters == 1: 
    print(f'{quarters} Quarter')
if quarters > 1:
    print(f'{quarters} Quarters')
if dimes == 1: 
    print(f'{dimes} Dime')
if dimes > 1:
    print(f'{dimes} Dimes')
if nickels == 1: 
    print(f'{nickels} Nickel')
if nickels > 1:
    print(f'{nickels} Nickels')
if pennies == 1: 
    print(f'{pennies} Penny')
if pennies > 1:
    print(f'{pennies} Pennies')


