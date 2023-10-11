# "R" pizza restaurant
rows, cols = [int(x) for x in input().split()]

matrix = []
moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
current_pos = []
boy_pos = []

for row in range(rows):
    field = input()
    matrix.append([el for el in field])
    if "B" in field:
        current_pos = [row, field.index('B')]
        boy_pos = [row, field.index('B')]

while True:
    command = input()

    current_pos = [current_pos[0] + moves[command][0],
                   current_pos[1] + moves[command][1]
                   ]

    if 0 > current_pos[0] or current_pos[0] >= rows or 0 > current_pos[1] or current_pos[1] >= cols:
        matrix[boy_pos[0]][boy_pos[1]] = ' '
        print("The delivery is late. Order is canceled.")
        break

    if matrix[current_pos[0]][current_pos[1]] == "-":
        matrix[current_pos[0]][current_pos[1]] = "."

    if matrix[current_pos[0]][current_pos[1]] == "P":
        matrix[current_pos[0]][current_pos[1]] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    if matrix[current_pos[0]][current_pos[1]] == "*":
        current_pos = [current_pos[0] - moves[command][0],
                       current_pos[1] - moves[command][1]
                       ]
        continue

    if matrix[current_pos[0]][current_pos[1]] == 'A':
        matrix[current_pos[0]][current_pos[1]] = "P"
        print("Pizza is delivered on time! Next order...")
        break

final = ''
for row in matrix:
    for el in row:
        final += el

    print(final)
    final = ''







