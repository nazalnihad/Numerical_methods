import numpy as np
def gauss_jordan_elimination(A,b):
    n = len(b)
    # print(n)

    for i in range(n-1):
        for j in range(i+1,n):
            fact = A[j,i]/A[i,i]
            # print(A[j,i:])
            A[j,i:]-=A[i,i:]*fact
            b[j]-=b[i]*fact
            # print(fact)
            print(A)
            print(b)
    
    for i in range(n-1,0,-1):
        for j in range(i-1,-1,-1):
            fact = A[j,i]/A[i,i]
            # print(A[j,i:])
            A[j,i:]-=A[i,i:]*fact
            b[j]-=b[i]*fact
            # print(fact)
            print(A)
            print(b)

    for i in range(n):
        b[i]/=A[i,i]
        A[i]/=A[i,i]

    # x = np.zeros_like(b)
    # x[-1] = b[-1] / A[-1, -1]
    # for i in range(n-2, -1, -1):
    #     x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    print(A,b)

A = np.array([[2, -1, 1], [3, 3, 9], [3, 3, 5]], dtype=float)
b = np.array([5, 15, 10], dtype=float)

gauss_jordan_elimination(A,b)