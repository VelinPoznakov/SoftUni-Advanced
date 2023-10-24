from collections import deque

armor = deque(int(x) for x in input().split(','))  # first
tricking = [int(x) for x in input().split(',')]  # last

killed_monsters = 0
# if t >= a monster killed and remove it decrease the t with a then add remaining a to the next a (if any)
# zero not push back

# if t < a reduse a remove t and add t to the back of the sq

while True:
    if tricking and armor:
        a = armor.popleft()
        t = tricking.pop(-1)

        if t >= a:
            killed_monsters += 1
            if t - a == 0:
                continue
            else:
                if tricking:
                    tricking[-1] += t - a
                else:
                    tricking.append(t - a)

        else:  # t < a
            armor.append(a - t)
    else:
        break


if not armor:
    print("All monsters have been killed!")
if not tricking:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")

