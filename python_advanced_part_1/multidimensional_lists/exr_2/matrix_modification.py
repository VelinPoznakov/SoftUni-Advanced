n = int(input())

matrix = [[int(x) for x in input().split()] for r in range(n)]

def is_valid(a, b, matrix):
    if 0 <= a <= len(matrix) - 1 and 0 <= b <= len(matrix) - 1:
        return True
    else:
        return False


while True:
    command = input().split()

    if command[0] == 'END':
        for el in matrix:
            print(*el)
        break

    if command[0] == 'Add':
        if is_valid(int(command[1]), int(command[2]), matrix):
            matrix[int(command[1])][int(command[2])] += int(command[3])
        else:
            print("Invalid coordinates")

    else:
        if is_valid(int(command[1]), int(command[2]), matrix):
            matrix[int(command[1])][int(command[2])] -= int(command[3])
        else:
            print("Invalid coordinates")

