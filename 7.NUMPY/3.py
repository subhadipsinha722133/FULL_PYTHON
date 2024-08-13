import numpy as np

x = [1, 2, 3, 4]
y = np.array(x)
print(y)
print(type(y))


l = []
for i in range(1, 11):
    a = input("enter no :-")
    l.append(a)
print(np.array(l))
