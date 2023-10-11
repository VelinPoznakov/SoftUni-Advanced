n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split()])


primary_diagonal = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n)]

print(abs(sum(primary_diagonal) - sum(secondary)))
