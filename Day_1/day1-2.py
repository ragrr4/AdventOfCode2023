
def replace_string_numbers(line):
    number_names = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replace_idx = []
    for i, number_str in enumerate(number_names):
        last_index_found = line.find(number_str,0)
        while(last_index_found != -1):
            line = line[:last_index_found + 1] + str(i+1) + line[last_index_found+1:]
            last_index_found = line.find(number_str,last_index_found + 1)
    return line

raw_input = []
result = 0
with(open("input.txt") as file):
    raw_input = file.read().splitlines()
for line in raw_input:
    line = replace_string_numbers(line)
    print(line)
    line_number = ''
    for c in line:
        if c.isdigit():
            line_number += c
            break
    for c in line[::-1]:
        if c.isdigit():
            line_number += c
            break
    result += int(line_number)
print(result)
#53312
