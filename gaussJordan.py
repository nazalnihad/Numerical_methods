import numpy as np

def gauss_jordan(A, b):
    n = A.shape[0]
    A = A.astype(float)
    b = b.astype(float)
    
    augmented = np.column_stack((A, b))
    
    for k in range(n):
        # Normalize the pivot row
        pivot = augmented[k, k]
        augmented[k, :] /= pivot
        
        for i in range(k + 1, n):
            factor = augmented[i, k]
            augmented[i, :] -= factor * augmented[k, :]
    
    for k in range(n - 1, -1, -1):
        for i in range(k):
            factor = augmented[i, k]
            augmented[i, :] -= factor * augmented[k, :]
    
    # Extract the solution vector
    x = augmented[:, n]
    
    return x

#  usage
A = np.array([[4, 2, 3], [2, 2, 1], [1, 1, 1]])
b = np.array([4, 6, 0])

x = gauss_jordan(A, b)
print(f"Solution: {x}")

# example 1
# A = np.array([[10, 1, 1], [1, 10, -1], [1, -2, 10]])
# b = np.array([12, 10, 9])
# Solution: [1. 1. 1.]

# example 2
# A = np.array([[4, 2, 3], [2, 2, 1], [1, 1, 1]])
# b = np.array([4, 6, 0])
# Solution: [ 5.  1. -6.]