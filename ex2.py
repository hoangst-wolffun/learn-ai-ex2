# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]

import numpy as np

array1 = np.random.randint(0, 20, 5)
array2 = np.random.randint(0, 20, 10)

print(array1)

print(array2)

result = np.in1d(array1, array2)

print(result)