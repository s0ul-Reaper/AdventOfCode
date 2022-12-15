with open('input.txt', 'r') as f:
    data = f.read()


def det(x, y):
    for i in range(len(x)):
        temp = x[i:i+y]
        if len(set(temp)) == len(temp):
            return i+y


print(
    f'The solution of part a is {det(data, 4)}\nThe solution of part b is {det(data, 14)}')


################ DONK SOLUTION ################

# def detective(x: str, y: int) -> int:
#     for i in range(len(x)):
#         if x[i:i+y].count(x[i]) == 1 and x[i:i+y].count(x[i+1]) == 1 and x[i:i+y].count(x[i+2]) == 1 and x[i:i+y].count(x[i+3]) == 1:
#             return i+y
#         else:
#             continue


# def detective2(x: str, y: int) -> int:
#     for i in range(len(x)):
#         if x[i:i+y].count(x[i]) == 1 and x[i:i+y].count(x[i+1]) == 1 and x[i:i+y].count(x[i+2]) == 1 and x[i:i+y].count(x[i+3]) == 1\
#             and x[i:i+y].count(x[i+y]) == 1 and x[i:i+y].count(x[i+5]) == 1 and x[i:i+y].count(x[i+6]) == 1 and x[i:i+y].count(x[i+7]) == 1\
#             and x[i:i+y].count(x[i+8]) == 1 and x[i:i+y].count(x[i+9]) == 1 and x[i:i+y].count(x[i+10]) == 1 and x[i:i+y].count(x[i+11]) == 1\
#                 and x[i:i+y].count(x[i+12]) == 1 and x[i:i+y].count(x[i+13]):
#             return i+y
#         else:
#             continue
