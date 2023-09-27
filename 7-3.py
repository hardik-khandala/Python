def skip_header(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            if not line.startswith('#') and not line.strip().startswith('Header'):
                print(line.strip())

file_name = 'data.txt'

skip_header(file_name)