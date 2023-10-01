def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid 
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = int(input("Enter a number to search for: "))
result = binary_search(my_list, target_value)

if result != -1:
    print(f"{target_value} found at index {result}")
else:
    print(f"{target_value} not found in the list")
