with open('input.txt', 'r') as f:
    temp = []
    for line in f:
        temp.append(line)

temp = [l.strip('\n') for l in temp]


c = 0
final = []

for i in range(len(temp)):
    if temp[i] != '':
        c += int(temp[i])
    else:
        final.append(c)
        c = 0

final = sorted(final)[-3::]

print(
    f'The answer of part 1 is: {max(final)}\nThe answer of part 2 is: {sum(final)}')
