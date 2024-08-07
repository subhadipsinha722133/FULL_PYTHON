def fact(n):
    """this is a function"""
    a=1
    while n>=1:
        a*=n
        n-=1
    return a
# The code is calculating the factorial of numbers from 1 to 9 and printing the result.
for i in range(1,10):
    print('factorial of {} is {}'.format(i,fact(i)))
 
print()
print()
print()


def factorial (n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))    






