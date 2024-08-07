import sys
sum = 0
while True :
    x = int ( input('enter a number '))
    if x== 999:
        sys.exit( 0 )
    sum += x
    print ('sum is ',sum)     