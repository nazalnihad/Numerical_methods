def evaluate_function(x, user_fun):
    return eval(user_fun)

def false_position(t):
    i = 0
    j = 0
    while evaluate_function(j, user_fun) * evaluate_function(j + 1, user_fun) > 0:
        j += 1
    a = j
    b = j + 1
    print("a:", a)
    print("b:", b)
    c = (a * evaluate_function(b, user_fun) - b * evaluate_function(a, user_fun)) / (evaluate_function(b, user_fun) - evaluate_function(a, user_fun))
    previous_c = None
    while True:
        previous_c = c
        f = evaluate_function(c, user_fun)
        if f < 0:
            a = c
        elif f > 0:
            b = c
        c = (a * evaluate_function(b, user_fun) - b * evaluate_function(a, user_fun)) / (evaluate_function(b, user_fun) - evaluate_function(a, user_fun))
        i += 1
        print("Iteration:", i)
        print("a:", a)
        print("b:", b)
        print("c:", c)
        if abs(previous_c - c) <= t:
            break
    print("Root:", c)

user_fun = input("Enter function: ")
false_position(0.005)
