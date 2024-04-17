import math

def func(x):
    if x <= 0:
        return 0
    return math.exp(-x)

def calc_trapezoidal_integral(lower, upper, n):
    if n <= 0:
        print("Number of intervals must be positive")
        return None

    h = (upper - lower) / n
    x = []
    y = []

    print("x\ty")
    for i in range(n + 1):
        x_value = lower + h * i
        y_value = func(x_value)
        x.append(x_value)
        y.append(y_value)
        print(f"{x_value:.2f}\t{y_value:.6f}")

    result = h * (0.5 * y[0] + sum(y[1:n]) + 0.5 * y[n])
    return result

answer = calc_trapezoidal_integral(0, 2, 6)
print(f"\nThe trapezoidal integral result is: {answer:.6f}")