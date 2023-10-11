def eat_cuccies(nice_kids_visited, presents):
    for value in moves.values():
        r = santa_pos[0] + value[0]
        c = santa_pos[1] + value[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                nice_kids_visited += 1

            presents -= 1
            neighborhood[r][c] = '-'

        if not all_presents:
            break

    return nice_kids_visited, presents


all_presents = int(input())  # Всички подаръци които се подават

n = int(input()) # колоните и реговете на матрицата

neighborhood = []  # Матрицата
santa_pos = [] # Позицията на героя
total_good_kids = 0  # Броя на добрите деца през които  е минато
nice_kids_visited = 0

moves = {  # кординатите за всяка команда която ще се изпълнява от героя
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for i in range(n):
    line = input().split()
    neighborhood.append(line)

    if 'S' in line:  # Проверява къде се намира santa
        santa_pos = [i, line.index('S')]  # Показва началаната позиция на santa
        neighborhood[i][santa_pos[1]] = '-'  # Заменя позицията на santa с "-"

    total_good_kids += line.count('V')

command = input()

while True:

    if command == 'Christmas morning':
        break

    santa_pos = [
        santa_pos[0] + moves[command][0],
        santa_pos[1] + moves[command][1]
    ]

    if neighborhood[santa_pos[0]][santa_pos[1]] == 'V':
        all_presents -= 1
        nice_kids_visited += 1

    elif neighborhood[santa_pos[0]][santa_pos[1]] == 'C':
        nice_kids_visited, all_presents = eat_cuccies(nice_kids_visited, all_presents)

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not all_presents or nice_kids_visited == total_good_kids:
        break
    command = input()
neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not all_presents and nice_kids_visited < total_good_kids:
    print("Santa ran out of presents!")

print(*[' '.join(c) for c in neighborhood], sep='\n')

if nice_kids_visited == total_good_kids:
    print(f"Good job, Santa! {nice_kids_visited} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - nice_kids_visited} nice kid/s.")


