# Countdown Example
def countdown(n):
    for i in range(n, -1, -1):
        print(i)

countdown(5)

# Add Up Numbers without Recursion
def addupNumbers(n):
    total = 0

    for i in range(n, 0, -1):
        total += i

    return total

print(addupNumbers(100)) # 5050

# Add Up Numbers with Recursion
def addupNumbers(n):
    if n == 1:
        return 1

    return n + addupNumbers(n-1)

print(addupNumbers(100)) # 5050
