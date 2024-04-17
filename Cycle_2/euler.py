def euler_method(f, x0, y0, Dx, n):
    x = [x0]
    y = [y0]
    for i in range(1, n+1):
        x.append(x[i-1] + Dx)
        y.append(y[i-1] + Dx * f(x[i-1], y[i-1]))
        print(f"Step {i}: x = {x[i]}, y = {y[i]:.4f}")
    return x, y

# Example function 
def f(x, y):
    return (y - x) / (y + x)


x0 = float(input("Enter initial x value: "))
y0 = float(input("Enter initial y value: "))
Dx = float(input("Enter step size (Dx): "))
n = int(input("Enter number of steps: "))

x_values, y_values = euler_method(f, x0, y0, Dx, n)
