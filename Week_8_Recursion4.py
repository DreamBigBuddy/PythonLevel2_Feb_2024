# Factorial Calculator
def factorial(n):
    if n == 1 or n == 0:
        return 1

    return n * factorial(n-1)

# Sum of List Template
def list_sum(nums):
    # Code goes here

numbers = [2, 6, 8, 3, 4, 10]
print(f"The sum of the list is: {list_sum(numbers)}")
