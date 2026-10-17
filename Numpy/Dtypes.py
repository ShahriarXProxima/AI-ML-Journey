import numpy as np

array = np.array(
    [1, 2, 3, 4, 5, 0], dtype=np.str_
)  # also can use int16 or int8. but there is a range in each category

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")
print()

strings = np.array(
    ["Shahriar", "Tahmid", "sabiha", "mishad", "abrar"], dtype="<U6"
)  # we can use "U1-n" to define the number of char in the string

print(strings)
print(strings.dtype)
print(f"{strings.nbytes} bytes")
print()

array = np.array(
    [1, True, "shahriar", 4, 3.0, 0], dtype=np.object_
)  # by object_ we can store any type of data in the array. but it doesn't use numpy anymore

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")
print()


array = np.array(
    [1, 2, 3, 4, 5, 0], dtype=np.str_
)  # also can use int16 or int8. but there is a range in each category

print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")
print()

array = array.astype(np.float16) # astype method can change the dtypw later
print(array)
print(array.dtype)
print(f"{array.nbytes} bytes")
print()