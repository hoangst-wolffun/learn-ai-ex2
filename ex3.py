# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]

import numpy as np

array = np.random.randint(0, 100, 50)

print(array)

index_max = np.argmax(array)

index_min = np.argmin(array)

print(f"The indices of maximum value is {index_max}")
print(f"The indices of minimum value is {index_min}")