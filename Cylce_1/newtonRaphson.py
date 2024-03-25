def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
   x=x0
   for i in range(max_iter):
        x_new = x - f(x) / df(x)

        if abs(x_new - x) < tol:
            return x_new, i+1

        x = x_new

if __name__ == "__main__":

    def f(x):
        #return x**2 - 4
        return x**6-x-1

    def df(x):
        return 6*x**5-1

    x0 = 2.0
    root,num_iter = newton_raphson(f,df,x0)
    print(root)
    print(num_iter)
