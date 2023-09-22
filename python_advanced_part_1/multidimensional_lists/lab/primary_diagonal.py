n = int(input())

matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split()])

the_sum = 0
for i in range(n):
    the_sum += matrix[i][i]

print(the_sum)

