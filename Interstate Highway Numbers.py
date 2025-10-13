''' Type your code here. '''
highwayNumber = int(input())
serviceHighway = highwayNumber % 100

# Type your code here
if highwayNumber == 0 or highwayNumber > 999 or highwayNumber % 100 == 00:
   print(f'{highwayNumber} is not a valid interstate highway number.')
elif highwayNumber >= 1 and highwayNumber <= 99:
   print(f'I-{highwayNumber} is primary', end = "")
elif highwayNumber >=100 and highwayNumber <= 999:
   print(f'I-{highwayNumber} is auxiliary, serving I-{serviceHighway}', end = "")

#Check for even or odd input
if highwayNumber % 2 == 0 and highwayNumber != 0 and highwayNumber < 1000 and highwayNumber % 100 != 00:
   print(", going east/west.")
if highwayNumber % 2 != 0 and highwayNumber != 0 and highwayNumber < 1000 and highwayNumber % 100 != 00:
   print(", going north/south.")
