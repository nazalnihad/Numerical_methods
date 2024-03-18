import math

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0
    
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result

n = int(input("Enter the number of data : "))

x_values = []
y_values = []

for i in range(n):
    print(f"Enter x{i} and y{i} :")
    x, y = map(float, input().split())
    x_values.append(x)
    y_values.append(y)

x = float(input("Enter the value of x to interpolate: "))

result = lagrange_interpolation(x_values, y_values, x)
print(f"The interpolated value at x = {x} is: {result}")