import math

def func(x):
    return math.exp(-x)

def calc_simpson_3_8_integral(lower, upper, n):
    if n % 3 != 0:
        print("incorrect interval")

    h = (upper - lower) / n
    x = []
    y = []
    i = 0
    while i <= n:
        x.append(lower + h * i)
        y.append(func(lower + h * i))
        i += 1

    print(x)
    print(y)

    result = 0
    for i in range(n + 1):
        if i == 0 or i == n:
            result += y[i]
        elif i % 3 == 0:
            result += 2 * y[i]
        else:
            result += 3 * y[i]

    result = (3 * h / 8) * result
    return result

answer = calc_simpson_3_8_integral(0, 2, 6)
print(f"integral value of the equation using simpson 3/8 is : {answer}")