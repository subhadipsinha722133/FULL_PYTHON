for i in range(10):
    print("{0:3} {1:10}".format(i, 10**i))
print()
# print(i)


b = 10
for row in range(1, b + 1):
    for column in range(1, b + 1):
        c = row * column
        print("{0:4}".format(c), end="")
    print()


a = "hello"
b = len(a)
for i in range(b):
    print(a[i])

a = [
    45,
    65,
    564,
    465,
    675,
    45,
    3456,
    564,
    5634,
    56,
    65,
    65,
    7453,
    654,
    465,
    76,
    547465,
    567,
]
for i in a:
    print(i)

a = str(input("enter name = "))
for first in a:
    for second in a:
        if first != second:
            for third in a:
                for firth in a:
                    if third != second != first != firth:
                        print(first + second + third + firth)
