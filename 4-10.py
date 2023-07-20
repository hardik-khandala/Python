def count_strings(strings):
    count = 0
    for string in strings:
        if len(string)>=2 and string[0]==string[-1]:
            count+=1
    return count

strings = ['Hello', 'wow', 'level', 'good']
print(count_strings(strings))
