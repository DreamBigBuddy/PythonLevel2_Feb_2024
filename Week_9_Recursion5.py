def list_sum(nums):
    if len(nums) == 0:
        return 0

    return nums[0] + list_sum(nums[1:])

numbers = [1, 4, 3, 5, 6]
print(f"Sum: {list_sum(numbers)}")
