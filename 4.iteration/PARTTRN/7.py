
n=8
for i in range(1,n+1):
    for j in range(n, i,- 1):
        print(" ",end='')
    for k in range(1, i + 1):
        print(i,end='')
    for l in range(i-1,0,-1):
        print(i,end='')
    print()
