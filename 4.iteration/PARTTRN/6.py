n=8
for i in range(1,n+1):
    for j in range(n, i,- 1):
        print(" ",end='')
    for k in range(1, i + 1):
        print(k,end='')
    for l in range(i-1,0,-1):
        print(l,end='')
    print()


#        1
#       121
#      12321
#     1234321
#    123454321
#   12345654321
#  1234567654321
# 123456787654321

n=8
for i in range(1,n+1):
    for j in range(n, i,- 1):
        print(" ",end='')
    for k in range(1, i + 1):
        print(i,end='')
    for l in range(i-1,0,-1):
        print(i,end='')
    print()
#        1
#       222
#      33333
#     4444444
#    555555555
#   66666666666
#  7777777777777
# 888888888888888