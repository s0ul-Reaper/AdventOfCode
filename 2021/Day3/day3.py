
with open('input.txt', 'r') as f:
    temp = []
    for line in f:
        temp.append(line)
    inputs = []
    for i in temp:
        inputs.append(i.strip('\n'))


def binary_to_dec(x):
    sum = 0
    for index, i in enumerate(x):
        sum += i * 2**(len(x)-index-1)

    return sum


gamma_rate = []
epsilon_rate = []
count_zeros = 0
count_ones = 0

for k in range(12):
    for i in (inputs):
        if i[k] == '0':
            count_zeros += 1
        else:
            count_ones += 1

    if count_zeros > count_ones:
        gamma_rate.append(0)
        epsilon_rate.append(1)
    else:
        gamma_rate.append(1)
        epsilon_rate.append(0)

    count_zeros = 0
    count_ones = 0

result1 = binary_to_dec(epsilon_rate) * binary_to_dec(gamma_rate)

"""### This is where part2 begins. """

start_0 = []
start_1 = []
count_0 = 0
count_1 = 0
oxygen = []
co2 = []
x = inputs
for idx in range(12):
    for value in x:
        if value[idx] == '0':
            count_0 += 1
            start_0.append(value)
        else:
            count_1 += 1
            start_1.append(value)
        if count_0 > count_1:
            oxygen = start_0
        else:
            oxygen = start_1
    x = oxygen
    start_0 = []
    start_1 = []
    count_0 = 0
    count_1 = 0
    if len(oxygen) == 1:
        final_ox = oxygen

    oxygen = []

y = inputs

for idx in range(12):
    for value in y:
        if value[idx] == '0':
            count_0 += 1
            start_0.append(value)
        else:
            count_1 += 1
            start_1.append(value)
        if count_0 > count_1:
            co2 = start_1
        else:
            co2 = start_0
    y = co2
    start_0 = []
    start_1 = []
    count_0 = 0
    count_1 = 0
    if len(co2) == 1:
        final_co2 = co2

    co2 = []

"""### Last step is to convert those binaries into decimal and multiply them. """

ogr = [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]  # oxygen generator rating
co2sr = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0]  # co2 scrubber rating

result2 = binary_to_dec(ogr) * binary_to_dec(co2sr)

print(
    f'The result of part one is: {result1}\nThe result of part two is: {result2} ')
