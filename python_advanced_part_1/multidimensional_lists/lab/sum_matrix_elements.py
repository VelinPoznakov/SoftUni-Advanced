# row, cols = [int(i) for i in input().split(', ')]
#
# matrix = []
#
# for v in range(row):
#     nums = [int(x) for x in input().split(', ')]
#     matrix.append(nums)
#
# sums = 0
#
# for idx in matrix:
#     sums += sum(idx)
#
# print(sums)
# print(matrix)


row, cols = [int(i) for i in input().split(', ')]

matrix = []

matrix.append([int(x) for x in input().split(', ')] for v in range(row))

print(sum(idx) for idx in matrix)
print(matrix)