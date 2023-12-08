raw_input = []
result = 0
with(open("input.txt") as file):
    raw_input = file.read().splitlines()
for line in raw_input:
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
#53386