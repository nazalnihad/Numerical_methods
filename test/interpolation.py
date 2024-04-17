import numpy as np

def newton_forward(x, y, x_new):
    """
    Perform Newton's forward interpolation.
    
    Parameters:
    x (numpy.ndarray): The independent variable data points.
    y (numpy.ndarray): The dependent variable data points.
    x_new (numpy.ndarray): The new independent variable points for interpolation.
    
    Returns:
    numpy.ndarray: The interpolated values at the new independent variable points.
    """
    n = len(x)
    y_new = []
    
    for x_i in x_new:
        # Calculate the divided difference table
        diff_table = np.zeros((n, n))
        diff_table[:, 0] = y
        
        for i in range(1, n):
            for j in range(n-i):
                diff_table[j, i] = (diff_table[j+1, i-1] - diff_table[j, i-1]) / (x[j+i] - x[j])
        
        # Calculate the interpolated value using Newton's forward formula
        y_i = diff_table[0, 0]
        h = x[1] - x[0]
        u = (x_i - x[0]) / h
        for i in range(1, n):
            y_i += diff_table[0, i] * np.prod([u-j for j in range(i)]) / np.math.factorial(i)
        y_new.append(y_i)
    
    return np.array(y_new)

def newton_backward(x, y, x_new):
    """
    Perform Newton's backward interpolation.
    
    Parameters:
    x (numpy.ndarray): The independent variable data points.
    y (numpy.ndarray): The dependent variable data points.
    x_new (numpy.ndarray): The new independent variable points for interpolation.
    
    Returns:
    numpy.ndarray: The interpolated values at the new independent variable points.
    """
    n = len(x)
    y_new = []
    
    for x_i in x_new:
        # Calculate the divided difference table
        diff_table = np.zeros((n, n))
        diff_table[:, 0] = y
        
        for i in range(1, n):
            for j in range(n-i):
                diff_table[j+i, i] = (diff_table[j+i, i-1] - diff_table[j+i-1, i-1]) / (x[j+i] - x[j])
        
        # Calculate the interpolated value using Newton's backward formula
        y_i = diff_table[-1, 0]
        h = x[1] - x[0]
        u = (x_i - x[-1]) / h
        for i in range(1, n):
            y_i += diff_table[-i-1, i] * np.prod([u+j for j in range(i)]) / np.math.factorial(i)
        y_new.append(y_i)
    
    return np.array(y_new)

# Example usage
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 7, 13, 21])
x_new = np.linspace(0, 4, 11)

# Forward interpolation
y_forward = newton_forward(x, y, x_new)
print("Forward interpolation:")
print(y_forward)

# Backward interpolation
y_backward = newton_backward(x, y, x_new)
print("Backward interpolation:")
print(y_backward)