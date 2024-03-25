import numpy as np

def gauss_seidel(A, b, x0, tol, max_iter):
    n = A.shape[0]
    x = np.copy(x0)
    
    for k in range(max_iter):
        x_old = np.copy(x)
        for i in range(n):
            s1 = sum(A[i, j] * x_old[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            x[i] = (b[i] - s1 - s2) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            break
    
    return x, k + 1

A = np.array([[4,-1, 0], [-1, 4, -1], [0, -1, 3]])
b = np.array([12, -1, 0])
x0 = np.array([0, 0, 0])
tol = 1e-6
max_iter = 100

x, num_iter = gauss_seidel(A, b, x0, tol, max_iter)
print(f"Solution: {x}")
print(f"Number of iterations: {num_iter}")

# example 1
# A = np.array([[4,-1, 0], [-1, 4, -1], [0, -1, 3]])
# b = np.array([12, -1, 0])
# Solution: [3 0 0]

# example 2
# A = np.array([[10,1, 1], [1, 10, -1], [1, -2, 10]])
# b = np.array([12, 10, 9])
# Solution: [1 0 1]