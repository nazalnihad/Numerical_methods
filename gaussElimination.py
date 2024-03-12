import numpy as np

def gaussian_elimination(A, b):
    n = A.shape[0]
    
    # Augment 
    augmented = np.column_stack((A, b))
    
    # forward elimination
    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = augmented[i, k] / augmented[k, k]
            for j in range(k, n + 1):
                augmented[i, j] -= factor * augmented[k, j]
    
    # substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented[i, n] - np.dot(augmented[i, :n], x)) / augmented[i, i]
    
    return x

A = np.array([[2, 1, -1], [4, 3, -2], [8, 7, -5]])
b = np.array([5, 7, 9])

x = gaussian_elimination(A, b)
print(f"Solution: {x}")