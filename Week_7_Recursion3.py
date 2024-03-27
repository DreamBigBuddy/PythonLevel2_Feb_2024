# Factorial Calculator
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"{num}! = {factorial(num)}")

# Return Statement Example
def test(n):
    return n

num = int(input("Enter a number: "))
a = test(num)
print(a)

