a = [3.3, 4, 6, -7.8, 8, -7, "hi", "end", 9]
for i in a:
    print(i)


print()

b = [32, 45, 5, 7.8, 9, 0.0, 0.9, "hi", "hello", 1]
for i in range(len(b)):
    print(b[i])

print()

b = [32, 45, 5, 7.8, 9, 0.0, 0.9, "hi", "hello", 1]
for i in range(len(b) - 1, -1, -1):
    print(b[i])
