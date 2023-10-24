hazelnuts = 0
field_range = int(input())

commands = [c for c in input().split(', ')]

field = []
sq_pos = []

move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(field_range):
    line = input()
    field.append([el for el in line])
    if 's' in line:
        sq_pos = [r, line.index('s')]
        field[sq_pos[0]][sq_pos[1]] = '*'

for command in commands:

    sq_pos = [sq_pos[0] + move[command][0],
              sq_pos[1] + move[command][1]
              ]

    if 0 > sq_pos[0] or sq_pos[0] >= field_range or 0 > sq_pos[1] or sq_pos[1] >= field_range:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()

    if field[sq_pos[0]][sq_pos[1]] == 'h':
        field[sq_pos[0]][sq_pos[1]] = '*'
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            print(f"Hazelnuts collected: {hazelnuts}")
            break

    if field[sq_pos[0]][sq_pos[1]] == 't':
        print("Unfortunately, the squirrel stepped on a trap...")
        print(f"Hazelnuts collected: {hazelnuts}")
        exit()


if field[sq_pos[0]][sq_pos[1]] == 't' and hazelnuts < 3:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts}")





