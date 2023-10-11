rows, cols = [int(i) for i in input().split()]

matrix = [[i for i in input().split()] for r in range(rows)]
couter = 0
for r in range(rows - 1):
    for c in range(cols - 1):
        first = matrix[r][c]
        second = matrix[r][c + 1]
        third = matrix[r + 1][c]
        fourth = matrix[r + 1][c + 1]
        if first == second == third == fourth:
            couter += 1

print(couter)