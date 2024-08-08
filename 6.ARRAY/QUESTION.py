# STORING STUDENT MARK INTO AN ARRAY AND FINDING TOTAL MARKS AND PERCENTAGE

from array import *
a=[int (i) for i in input('enter marks :').split(',')]
marks=array('i',a)
sum=0
for i in marks:
    print(i)
    sum+=i
print('total marks =',sum)
n=len(marks)
percent=sum/n
print(percent)



