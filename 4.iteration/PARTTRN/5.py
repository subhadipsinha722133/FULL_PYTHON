n=8
for i in range(1,n+1):
    for j in range(n, i,- 1):
        print(" ",end='')
    for k in range(1, i + 1):
        print(k,end='')
    print()

#        1
#       12
#      123
#     1234
#    12345
#   123456
#  1234567
# 12345678

n=8
for i in range(1,n+1):
    for j in range(n, i,- 1):
        print(" ",end='')
    for k in range(1, i + 1):
        print(i,end='')
    print()

#        1
#       22
#      333
#     4444
#    55555
#   666666
#  7777777
# 88888888