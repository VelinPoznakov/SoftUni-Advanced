rows, cols = [int(x) for x in input().split()]

matrix = [[i for i in input().split()] for r in range(rows)]

while True:
    command = input().split()

    if command[0] == 'END':
        break
    try:
        matrix[int(command[1])][int(command[2])], matrix[int(command[3])][int(command[4])] = matrix[int(command[3])][int(command[4])],  matrix[int(command[1])][int(command[2])]
    except IndexError:
        print("Invalid input!")
        continue
    for i in matrix:
        print(*i)


