from array import*
x=array('i',[])
# print("how manny element?",end='')
n=int(input("how manny element?=" ))
for i in range(n):
    print("enter the element=",end='')
    x.append(int(input()))
print("all element is =",x)   

print("enter the element to be searh=",end='')
s=int (input())
p=x.index(s)
print("found the position=",p)


