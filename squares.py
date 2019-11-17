#week4 17.11.2019


squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = list(map(lambda x: x**2, range(10)))

squares = [x**2 for x in range(10)]


[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(x, y) for x in [2,5,6,3] for y in [4,3,6,5] if x == y]

combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))

combs

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[x.strip() for x in freshfruit]


[(x, x**2) for x in range(6)]

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

num = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 1, 9], [4, 9, 3, 6, 8, 3]]

num[0][3]
num[2][2]
num[1][4]
num[2][4]
num[0][0]
num[]

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]

for i in range(4):
    for row in matrix:
        row[i]


for x in range(10):
    for y in range(10):

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed

transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed
