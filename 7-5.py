def calculate_average(file_name):
    total = 0
    count = 0

    with open(file_name, 'r') as file:
        for line in file:
            values = line.strip().split()  
            for value in values:
                if value != '-':
                    try:
                        num = float(value)
                        total += num
                        count += 1
                    except ValueError:
                        pass  

    if count > 0:
        average = total / count
        return average
    else:
        return None 

file_name = 'data_with_hyphens.txt'

average_value = calculate_average(file_name)

if average_value is not None:
    print(f"The average of numeric values in '{file_name}' is: {average_value:.2f}")
else:
    print(f"No valid numeric values found in '{file_name}'.")
