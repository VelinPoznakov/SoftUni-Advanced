n = int(input())

matrix = []

for _ in range(n):
    matrix.append([x for x in input()])

symbol = input()

for r in range(len(matrix)):
    for c in range(len(matrix)):
        if symbol == matrix[r][c]:
            print((r, c,))
            exit()

print(f"{symbol} does not occur in the matrix")
