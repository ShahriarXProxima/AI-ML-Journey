import numpy as np

array = np.array(
    [
        ["a", "b", "c", "d"],
        ["a", "b", "c", "d"],
        ["a", "b", "c", "d"],
        ["1", "2", "3", "4"],
    ]
)  # 2 dimention

print(array)
print(array.ndim)
print()

# slicing is array[start:end:step]
print(array[0:4:2]) # row
print()
print(array[:,0:3:2]) #column