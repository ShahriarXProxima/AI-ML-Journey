import numpy as np

li = [1, 2, 3, 3, 4, 5, 6, 100, 20000, 1000000]
array = np.array(li)

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))