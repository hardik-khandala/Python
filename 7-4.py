def find_smallest_value(file_name):
    smallest = None
    with open(file_name, 'r') as file:
        for line in file:
            try:
                number = float(line.strip()) 
                if smallest is None or number < smallest:
                    smallest = number
            except ValueError:
                pass
    return smallest

file_name = 'data.txt'
smallest_value = find_smallest_value(file_name)

if smallest_value is not None:
    print(f"The smallest value in '{file_name}' is: {smallest_value}")
else:
    print(f"No valid numbers found in '{file_name}'.")
