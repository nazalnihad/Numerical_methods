import math

def func(x):
    return math.exp(-x)

def calc_simpson_integral(lower,upper,n):
    h = (upper-lower)/n
    x = []
    y = []

    i = 0
    while i<=n:
        x.append(lower+h*i)
        y.append(func(lower+h*i))
        i+=1

    
    print(x)
    print(y)

    result = 0
    for i in range(n+1):
        # print(y[i])
        if i==0 or i==n:
            # print(y[i])
            result+=y[i]
        elif i%2==0:
            result+=2*(y[i])
        else:
            result+=4*(y[i])
    result = (h/3)*result

    return result

answer = calc_simpson_integral(0,2,4)
print(f"integral value of the equation using simpson 1/3 is : {answer}")