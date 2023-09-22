rows, cols = [int(i) for i in input().split(',')]

matrix = []

for row in range(rows):
    matrix.append([int(r) for r in input().split()])

for col in range(cols):
    res = 0
    for row in range(rows):
        res += matrix[row][col]
    print(res)
