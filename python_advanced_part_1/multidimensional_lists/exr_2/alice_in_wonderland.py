n = int(input())

matrix = []
alice_positon = []

tea_bags_quality = 0

commands = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for r in range(n):
    line = input().split()
    matrix.append(line)

    if "A" in line:
        alice_positon = [r, line.index("A")]
        matrix[alice_positon[0]][alice_positon[1]] = "*"

while tea_bags_quality < 10:
    command = input()

    alice_positon = [alice_positon[0] + commands[command][0],
                     alice_positon[1] + commands[command][1]
                     ]
    if 0 > alice_positon[0] or alice_positon[0] >= n or 0 > alice_positon[1] or alice_positon[1] >= n:
        break

    if matrix[alice_positon[0]][alice_positon[1]].isdigit():
        tea_bags_quality += int(matrix[alice_positon[0]][alice_positon[1]])
        matrix[alice_positon[0]][alice_positon[1]] = '*'

    if matrix[alice_positon[0]][alice_positon[1]] == "R":
        matrix[alice_positon[0]][alice_positon[1]] = '*'
        break

    matrix[alice_positon[0]][alice_positon[1]] = '*'

if tea_bags_quality >= 10:
    print("She did it! She went to the party.")

else:
    print("Alice didn't make it to the tea party.")

for i in matrix:
    print(*i)
