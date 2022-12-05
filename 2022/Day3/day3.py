with open('input.txt', 'r') as f:
    data = [line for line in f]
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
print(f'The result of part one is: {result}')
