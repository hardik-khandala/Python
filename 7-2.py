def process_numbers(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            num1, num2 = map(int, line.strip().split())

            add = num1 + num2
            mul = num1 * num2

            outfile.write(f"Addition of {num1} and {num2} is {add}\n")
            outfile.write(f"Multiplication of {num1} and {num2} is {mul}\n")

input_file_name = 'file1.txt'
output_file_name = 'file2.txt'

process_numbers(input_file_name, output_file_name)