n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(', ')])


primary_diagonal = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - i - 1] for i in range(n)]

print(f"Primary diagonal: {', '.join([str(i) for i in primary_diagonal])}. Sum: {sum(primary_diagonal)}")

print(f"Secondary diagonal: {', '.join([str(i) for i in secondary])}. Sum: {sum(secondary)}")
