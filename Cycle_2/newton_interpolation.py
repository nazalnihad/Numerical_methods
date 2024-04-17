# write a program to estimate the value of a function for any intermediate value 
# of the independent variable using newton forward interpolation method
import math

def forward_difference(x, y, n):
    
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y[i]

    for i in range(1, n):
        for j in range(n - i):
            table[j][i] = table[j + 1][i - 1] - table[j][i - 1]
            print(table)
    
    return table

def forward_interpolation(x, y, x_val):
    n = len(x)
    h = x[1] - x[0]
    p = (x_val - x[0]) / h
    
    table = forward_difference(x, y, n)

    result = y[0]
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (p - j)
            term /= (j + 1)
        result += term * table[0][i]
    
    return result

def backward_interpolation(x, y, x_val):
    n = len(x)
    h = x[1] - x[0]
    p = (x_val - x[n - 1]) / h
    
    table = forward_difference(x, y, n)

    result = y[n - 1]
    for i in range(1, n):
        term = 1
        for j in range(i):
            term *= (p + j)
            term /= (j + 1)
        result += term * table[n - i - 1][i]
    
    return result

n = int(input("Enter no of arguments: "))
x = [0] * n  
y = [0] * n  

for i in range(n):
    x[i] = float(input(f"\nX {i}: "))
    y[i] = float(input(f"y {i}: "))

x_val = float(input("Enter the value of x to estimate f(x): "))

if abs(x_val - x[0]) < abs(x_val - x[n - 1]):
    result = forward_interpolation(x, y, x_val)
    print(f"The estimated value of f({x_val}) using forward interpolation is: {result}")
else:
    result = backward_interpolation(x, y, x_val)
    print(f"The estimated value of f({x_val}) using backward interpolation is: {result}")
 