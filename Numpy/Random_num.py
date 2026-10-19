import numpy as np

rng = np.random.default_rng()
print(rng.integers(low=1, high=7))


# shuffle an array
array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# random choice
array = rng.choice(array)
print(array)