from collections import deque

armor = deque(int(x) for x in input().split(","))

soldier = [int(y) for y in input().split(",")]

counter_monsters = 0

while armor and soldier:

    current_armor, current_soldiers = armor.popleft(), soldier.pop()

    if current_armor <= current_soldiers:
        counter_monsters += 1
        soldier[-1] += current_soldiers - current_armor

    else:
        armor.append(current_armor - current_soldiers)


if not armor:
    print("All monsters have been killed!")
else:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {counter_monsters}")
