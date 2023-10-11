rows, cols = [int(i) for i in input().split(',')]

cutboard = []
curr_mouse_pos = []
cheese_count = 0
move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(rows):
    line = input()
    cutboard.append([el for el in line])

    if 'M' in line:
        curr_mouse_pos = [row, line.index('M')]
        cutboard[row][curr_mouse_pos[1]] = '*'

    if 'C' in line:
        cheese_count += line.count('C')

while True:
    command = input()

    if cheese_count and command == 'danger':
        print("Mouse will come back later!")
        cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] = 'M'
        break

    curr_mouse_pos = [curr_mouse_pos[0] + move[command][0],
                      curr_mouse_pos[1] + move[command][1]
                      ]
    if 0 > curr_mouse_pos[0] or curr_mouse_pos[0] >= rows or 0 > curr_mouse_pos[1] or curr_mouse_pos[1] >= cols:
        curr_mouse_pos = [curr_mouse_pos[0] - move[command][0],
                          curr_mouse_pos[1] - move[command][1]
                          ]
        cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] = 'M'
        print("No more cheese for tonight!")
        break

    if cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] == 'C':
        cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] = '*'
        cheese_count -= 1
        if cheese_count == 0:
            cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] = 'M'
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    if cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] == 'T':
        cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] = 'M'
        print("Mouse is trapped!")
        break

    if cutboard[curr_mouse_pos[0]][curr_mouse_pos[1]] == '@':
        curr_mouse_pos = [curr_mouse_pos[0] - move[command][0],
                          curr_mouse_pos[1] - move[command][1]
                          ]
        continue

for r in cutboard:
    print(''.join(r))

