# tuples cannot be changed. just like strings

a = (2, 1, 2, 1, False, True, 2, 2, 2, 2)
print(type(a))
print(a[0])

no = a.count(2)
print(no)

i = a.index(False)
print(i)
