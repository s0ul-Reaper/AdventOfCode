
with open('input.txt', 'r') as f:
    temp = []
    for line in f:
        temp.append(line)
    inputs = []
    for i in temp:
        inputs.append(i.strip('\n'))


def string_to_num(x):
    nums = []
    for i in range(len(x)):
        nums.append(float(x[i]))

    return nums


forward = []
down = []
up = []

for i in inputs:
    if len(i) == 9:
        forward.append(i[-1])
    elif len(i) == 6:
        down.append(i[-1])
    else:
        up.append(i[-1])

fr = string_to_num(forward)
d = string_to_num(down)
u = string_to_num(up)

ud = sum(d) - sum(u)

result1 = int(sum(fr) * ud)

horizontal = 0
aim = 0
depth = 0
for i in inputs:
    if len(i) == 6:
        aim += int(i[-1])

    elif len(i) == 4:
        aim -= int(i[-1])

    else:
        horizontal += int(i[-1])
        depth += aim * int(i[-1])

result2 = horizontal * depth

print(
    f'The result of part one is: {result1}\nThe result of part two is: {result2} ')
