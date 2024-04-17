import numpy as np

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

def gauss_jordan_verbose(A, b):
    n = A.shape[0]
    A = A.astype(float)
    b = b.astype(float)

    augmented = np.column_stack((A, b))
    print("Initial Augmented Matrix:")
    print_matrix(augmented)
    print("\n")

    for k in range(n):
        # Normalize the pivot row
        pivot = augmented[k, k]
        augmented[k, :] /= pivot
        print(f"After pivot row normalization at step {k+1}:")
        print_matrix(augmented)
        print("\n")

        for i in range(k + 1, n):
            factor = augmented[i, k]
            augmented[i, :] -= factor * augmented[k, :]
    
    for k in range(n - 1, -1, -1):
        for i in range(k):
            factor = augmented[i, k]
            augmented[i, :] -= factor * augmented[k, :]

    print("Final Augmented Matrix:")
    print_matrix(augmented)
    print("\n")
    
    # Extract the solution vector
    x = augmented[:, n]
    
    return x

# Usage
A = np.array([[4, 2, 3], [2, 2, 1], [1, 1, 1]])
b = np.array([4, 6, 0])

x = gauss_jordan_verbose(A, b)
print(f"Solution: {x}")
