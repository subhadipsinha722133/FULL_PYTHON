import numpy as np

a = np.array([[1, 2, 3, 4], [4, 3, 2, 1]])
print(a)
print(a.ndim)  # dimantion

print()


b = np.array([[[1, 2, 3, 4], [4, 5, 6, 7], [9, 8, 7, 5]]])
print(b)
print(b.ndim)


print()

c = np.array([1, 2, 3], ndmin=10)
print(c)
print(c.ndim)
