
'''
The min_max_dictionary.py module provides a function to find the minimum and maximum values in a dictionary of ages. The function `find_min_max_dictionary` takes a dictionary of ages as input and returns the keys and values of the minimum and maximum ages.
'''

def find_min_max_dictionary(ages):
    if not ages:
        raise ValueError("Give find_min_max_dictionary at least one age")
    items_iterator = iter(ages.items())
    
    min_key, min_value = next(items_iterator)
    max_key = min_key
    max_value = min_value

    for key, value in items_iterator:

        if value < min_value:
            min_key = key
            min_value = value

        if value > max_value:
            max_key = key
            max_value = value
    return min_key, min_value, max_key, max_value

if __name__ == "__main__":
    ages = {
    "Alice" : 84,
    "Bob": 71,
    "Charlie": 96,
    "Diana": 88,
    "Eve": 67
    } # type: ignore
    mini_key, mini_value, maxi_key, maxi_value = find_min_max_dictionary(ages)
    print(f"The youngest: {mini_key} is {mini_value} years old")
    print(f"The oldest: {maxi_key} is {maxi_value} years old")
