def have_common_member(list1, list2):
    return any(item in list2 for item in list1)

# Test the function
list_a = [1, 2, 3, 4]
list_b = [3, 5, 6, 7]
list_c = [8, 9, 10]

print(have_common_member(list_a, list_b))  # Output: True
print(have_common_member(list_a, list_c))  # Output: False
