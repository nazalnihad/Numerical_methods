def bisection(f, a, b, e, iteration=1):
    c = (a+b)/2
    if (b-c <= e):
        return c
    elif (f(b)*f(c) <= 0):
        a = c
    else:
        b = c

    print(f"====={iteration}=====")
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("==========")

    return bisection(f, a, b, e, iteration+1)


def func(x):
    return x**6-x-1


def initial_vals():
    c = 0
    a = func(c)
    b = func(c+1)
    i = 0
    while (True):
        if (a < 0 and b > 0):
            return a, b
        else:
            i += 1
            c += 1
            a = b
            b = func(c)


def main():

    a, b = initial_vals()
    # print(a, b)
    root = bisection(func, a, b, 0.00005)
    print("Root for the equation is :", root)


if __name__ == "__main__":
    main()
