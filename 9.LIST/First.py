lst = [3, 54, 87, 987, 456, -56, -456, 67]
print(lst)
print()

print(lst[0])
print([3, 54, 87, 987, 456, -56, -456, 67])

for i in lst[:5]:
    print(i)
print()

lst[0] = 90
print(lst[3])
print(lst[0])

print()


def main():
    data = [45, 6, 765, 786, 879, 987, 987, 567, 645, 567, 78]
    print(data[-2])
    print(data[-7])
    print(data[-1])
    print(data[-0])
    print(data[-6])
    print(data[-3])
    print(data[-5])


main()
