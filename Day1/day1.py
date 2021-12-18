with open('input.txt', 'r') as f:
    temp = []
    for line in f:
        temp.append(line)

num = []
for i in temp:
    num.append(i.strip('\n'))


def string_to_num(x):
    nums = []
    for i in range(len(x)):
        nums.append(float(x[i]))

    return nums


numbers = string_to_num(num)


def sum_of_incr(x):

    counter = 0

    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            counter += 1

    return counter


sum_of_incr(numbers)


def add_per_three(x):

    sum3 = []
    for i in range(len(x)):
        if len(x[i:i+3]) == 3:
            c = 0
            c = x[i:i+3]
        sum3.append(sum(c))

    return sum3[:-2]


result1 = sum_of_incr(numbers)
result2 = sum_of_incr(add_per_three(numbers))

print(
    f'The result of part one is: {result1}\nThe result of part two is: {result2} ')
