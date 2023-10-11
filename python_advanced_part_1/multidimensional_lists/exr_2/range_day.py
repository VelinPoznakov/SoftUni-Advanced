def index_validator(shoother_pos, target_pos, command):
    while True:
        movement = [shoother_pos[0] + shoot[command[1]][0], shoother_pos[1] + shoot[command[1]][1]]
        if movement in target_pos:
            target_pos.remove(movement)
            movement = '.'
            return movement

SIZE = 5

matrix = []
shoother_pos = []
target_pos = []

move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
shoot = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(SIZE):
    line = input().split()
    matrix.append(line)

    if "A" in line:
        shoother_pos = [r, line.index("A")]

    if 'x' in line:
        target_pos = [r, line.index("x")]

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == 'shoot':
        index_validator(shoother_pos, target_pos, command)
    else:
        pass