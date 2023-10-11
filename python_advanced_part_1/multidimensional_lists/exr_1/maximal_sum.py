rows, cols = [int(x) for x in input().split()]

matrix = [[int(i) for i in input().split()] for r in range(rows)]

max_sum = float("-inf")  # Initialize max_sum to negative infinity
mx_sum_matrix = []

for c in range(cols - 2):
    for r in range(rows - 2):
        v1 = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2]
        v2 = matrix[r + 1][c] + matrix[r + 1][c + 1] + matrix[r + 1][c + 2]
        v3 = matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
        the_sum = v1 + v2 + v3

        if the_sum > max_sum:
            max_sum = the_sum
            mx_sum_matrix = [[matrix[r][c], matrix[r][c + 1], matrix[r][c + 2]],
                             [matrix[r + 1][c], matrix[r + 1][c + 1], matrix[r + 1][c + 2]],
                             [matrix[r + 2][c], matrix[r + 2][c + 1], matrix[r + 2][c + 2]]]

print(f"Sum = {max_sum}")
for i in mx_sum_matrix:
    print(*i)
