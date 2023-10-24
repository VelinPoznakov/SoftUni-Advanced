def invalid(s_pos):
    if s_pos[0] == -1:
        s_pos[0] = n - 1

    elif s_pos[0] == n:
        s_pos[0] = 0

    elif s_pos[1] == -1:
        s_pos[1] = n - 1

    else:
        s_pos[1] = 0


n = int(input())

area = []
s_pos = []
amount = 0

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(n):
    line = input()
    area.append([l for l in line])
    if 'S' in line:
        s_pos = [i, line.index('S')]
        area[s_pos[i]][s_pos[1]] = '-'

while True:
    command = input()

    if command == "collect the nets":
        break

    s_pos = [s_pos[0] + commands[command][0],
             s_pos[1] + commands[command][1]
             ]

    if 0 > s_pos[0] or s_pos[0] >= n or 0 > s_pos[1] or s_pos[1] >= n:
        invalid(s_pos)

    if area[s_pos[0]][s_pos[1]].isdigit():
        amount += int(area[s_pos[0]][s_pos[1]])
        area[s_pos[0]][s_pos[1]] = '-'

    if area[s_pos[0]][s_pos[1]] == 'W':
        print(
            f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{','.join(str(i) for i in s_pos)}]")
        exit()

area[s_pos[0]][s_pos[1]] = 'S'

if amount >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - amount} tons of fish more.")

if amount > 0:
    print(f"Amount of fish caught: {amount} tons.")

for l in area:
    print(''.join([str(a) for a in l]))
