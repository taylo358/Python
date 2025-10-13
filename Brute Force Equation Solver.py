''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

''' Type your code here. '''
def find_solution(a, b, c, d, e, f):
    # Iterate over all possible values of x
    for x in range(-10, 11):
        # Iterate over all possible values of y
        for y in range(-10, 11):
            # Check if the current (x, y) satisfies both equations
            if a * x + b * y == c and d * x + e * y == f:
                print(f"x = {x} , y = {y}")
                return
    # If no solution is found, output this message
    print("There is no solution")
    
if __name__ == "__main__":
    find_solution(a, b, c, d, e, f)
