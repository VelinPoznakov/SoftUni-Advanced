rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for r in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

max_el = float('-inf')
final_matrix = []
for col in range(cols - 1):
    for row in range(rows - 1):
        concurrent_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if concurrent_sum > max_el:
            max_el = concurrent_sum
            final_matrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]

print(*final_matrix[0])
print(*final_matrix[1])
print(max_el)
