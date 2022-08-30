nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):

    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]


def choose_func(numbers, func1, func2):
    processed = list(filter(lambda x: x < 0, numbers))
    if len(processed) == 0:
        return func1(numbers)
    else:
        return func2(numbers)

print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))

"""def choose_func(numbers, func1, func2):
    processed = list(filter(lambda x: x > 0, numbers))
    if len(processed) == 0:
        return func1(numbers)
    else:
        return func2(numbers)"""


