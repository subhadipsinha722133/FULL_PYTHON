from numpy import *

m = matrix("1 2 3 ;4 5 6;7 8 5")
print(m)


n = diagonal(m)
print(n)


k = m.min()
print(k)


x = m.max()
print(x)
