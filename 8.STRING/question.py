# a python program to access each element of a string in forward and reverse order using while loop.


str = " core python "
n = len(str)
i = 0
while i < n:
    print(str[i], end="")
    i += 1
print()

i=-1
while i>=-n:
    print(str[i],end=' ')
    i-=1
print()


 # using for loop
for b in str:
    print( b, end='')
print()
for b in str [: : -1]:
    print(b, end='')

















