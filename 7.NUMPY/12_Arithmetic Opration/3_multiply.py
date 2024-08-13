import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = a * 10
print(b)


print()


aa = np.array([1, 2, 3, 4, 5, 6, 7, 8])
bb = np.array([1, 3, 2, 9, 2, 3, 6, 8])

cc = aa * bb
print(cc)


print()


aa = np.array([[1, 2, 3, 4, 5], [5, 4, 3, 2, 7]])
bb = np.array([[5, 5, 9, 7, 0], [4, 5, 6, 6, 8]])

cc = aa * bb
print(cc)
