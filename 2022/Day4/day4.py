with open('input.txt', 'r') as f:
    input = [line.replace('\n', '').replace('-', ',').split(',') for line in f]


def to_int(x: list): return list(map(lambda x: int(x), x))


data = [to_int(i) for i in input]

a, b, c, d = 0, 1, 2, 3

counter = 0
for x in data:
    if (x[c] >= x[a] and x[d] <= x[b]) or (x[a] >= x[c] and x[b] <= x[d]):
        counter += 1

# Part b

counter2 = 0

for x in data:
    if (x[a] <= x[c] <= x[b]) or (x[c] <= x[a] <= x[d]):
        counter2 += 1

print(
    f'The result of part one is: {counter}\nThe result of part two is: {counter2}')
