with open('input.txt', 'r') as f:
    data = [line.replace('\n', '') for line in f]
with open('input.txt', 'r') as g:
    temp = g.read().replace('\n', '')


# import string
# lowercase = [letter for letter in string.ascii_lowercase]
# uppercase = [letter for letter in string.ascii_uppercase]
# alphabet = lowercase + uppercase


CHARS = list(set(temp))
MISSING_CHARS = ['a', 'e', 'i', 'k', 'o', 'u', 'x', 'y']
UPPER_MISSING_CHARS = [u.upper() for u in MISSING_CHARS]

alphabet = CHARS + MISSING_CHARS + UPPER_MISSING_CHARS
alphabet.sort(key=lambda x: (not x.islower(), x))

map = {}

for i in range(1, len(alphabet)+1):
    map[alphabet[i-1]] = i


def first_half(x): return x[:int(len(x)/2)]
def second_half(x): return x[int(len(x)/2)::]


flist = []

for final in data:
    flist.append(list(set(first_half(final)).intersection(
        second_half(final)))[0])

result = sum([map[k] for k in flist])

# Part b


common_badge = []

# for i in list(set(data[0])):
#     if i in list(set(data[1])):
#         t.append(i)
# for i in t:
#     if i in list(set(data[2])):
#         common_badge.append(i)


for n in range(0, len(data), 3):
    t = []
    for i in list(set(data[n])):
        if i in list(set(data[n+1])):
            t.append(i)
    for i in t:
        if i in list(set(data[n+2])):
            common_badge.append(i)

result2 = sum([map[k] for k in common_badge])


print(
    f'The result of part one is: {result}\nThe result of part two is: {result2}')
