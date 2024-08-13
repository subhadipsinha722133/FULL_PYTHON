import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a % 8
print(b)


print()


aa = np.array([1, 20, 30, 409, 5, 6, 70, 8])
bb = np.array([1, 2, 3, 4, 5, 66, 7, 8])

cc = aa % bb
print(cc)


print()


aa = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 7]])
bb = np.array([[5, 5, 9, 7, 9], [4, 5, 6, 6, 8]])

cc = aa % bb
print(cc)
