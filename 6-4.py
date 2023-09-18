def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return num == armstrong_sum

start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

numbers = list(range(start_range, end_range + 1))

armstrong_numbers = list(filter(is_armstrong, numbers))

print(f"Armstrong numbers in the range {start_range} to {end_range}: {armstrong_numbers}")
