def find_min_max(numbers):

    if not numbers:
        raise ValueError("Give find_min_max at least one number")

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers[1:]:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return smallest, largest
    





if __name__ == "__main__":
    numbers = [7, 2, 9, 4, 1, 8, 0 , 11, -1, 23]
    # Test 1
    #numbers = [42]

    # Test 2
    #numbers = [-10, -5, -100, -1]

    # Test 3
    #numbers = [5, 5, 5, 5, 5]

    # Test 4
    #numbers = [100, 90, 80, 70, 60]

    # Test 5
    #numbers = []
    smallest_number, largest_number = find_min_max(numbers)

    print(f"Smallest number = {smallest_number}")
    print(f"Largest number = {largest_number}")

