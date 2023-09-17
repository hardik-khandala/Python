def find_dups(input_list):
    duplicates = set()
    seen = set()
    
    for num in input_list:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return duplicates

input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
result = find_dups(input_list)
print("Duplicates:", result)
