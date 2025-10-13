import math

note = int(input())
r = math.pow(2,(1/12))

print(f'{note:.2f} Hz')
print(f'{note * math.pow(r,1):.2f} Hz')
print(f'{note * math.pow(r,2):.2f} Hz')
print(f'{note * math.pow(r,3):.2f} Hz')
