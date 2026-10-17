import numpy as np

array = np.array("a")  # 0 dimention
print(array)
print(array.ndim)
print()

array = np.array(["a", "b", "c", "d"])  # 1 dimention
print(array)
print(array.ndim)
print()

array = np.array(
    [["a", "b", "c", "d"], ["a", "b", "c", "d"], ["a", "b", "c", "d"]]
)  # 2 dimention
print(array)
print(array.ndim)
print()

array = np.array(
    [
        [["a", "b", "c", "d"], ["a", "b", "c", "d"], ["a", "b", "c", "d"]],
        [["a", "b", "c", "d"], ["a", "b", "c", "d"], ["a", "b", "c", "d"]],
        [["a", "b", "c", "d"], ["a", "b", "c", "d"], ["a", "b", "c", "d"]],
    ]
)  # 3 dimention
print(array)
print(array.ndim)
print(array.shape)
print(array[1, 1, 1]) # would prinnt 'b'
print()
