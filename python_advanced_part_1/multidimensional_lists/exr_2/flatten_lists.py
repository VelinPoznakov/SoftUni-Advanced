sequance = input().split('|')

new = []

for value in range(1, len(sequance) + 1):
    new.append(sequance[-value])

print(*new)


