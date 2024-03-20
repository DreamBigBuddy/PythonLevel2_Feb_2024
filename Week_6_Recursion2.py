def countdown(n):
    for i in range(n, -1, -1):
        print(i)

countdown(5)

def addupNumbers(n):
    total = 0

    for i in range(n, 0, -1):
        total += i

    return total

print(addupNumbers(100))
