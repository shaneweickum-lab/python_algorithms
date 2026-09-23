# Binary search algorithm implementation in Python

numbers = [2, 5, 8, 12, 16, 23, 31, 38, 45, 56, 67, 78, 89]
target = 56


def b_search(numbers, target):
    small = 0
    large = len(numbers) - 1
    while small <= large:
        middle = (small + large) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            small = middle + 1
        else:
            large = middle - 1
    return -1

print(f"Index of {target} in the list is: {b_search(numbers, target)}")
