import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array = array.reshape(3, 4)  # .reshape(rows, columns)
print(array)
print(array.ndim)

array = array.reshape(2, 2, 3)  # .reshape(layers, rows, columns)
print(array)
print(array.ndim)

array = array.reshape(-1, 1)  # reshape in a column
print(array)
print(array.ndim)

array = array.reshape(1, -1)  # reshape in a row
print(array)
print(array.ndim)
