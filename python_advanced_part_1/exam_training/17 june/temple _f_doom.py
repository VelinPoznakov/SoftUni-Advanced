from collections import deque

tools = deque(int(i) for i in input().split())  #hqueue popleft
substances = [int(i) for i in input().split()]  #stack iem.pop(-1)
challenges = [int(i) for i in input().split()]  # normal comprehension

while challenges:
    t = tools.popleft()
    s = substances.pop(-1)

    if t * s in challenges:
        challenges.remove(t * s)

    else:
        t += 1
        tools.append(t)
        if s - 1 > 0:
            substances.append(s - 1)

    if not substances or not substances and challenges:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join([str(t) for t in tools])}")
if substances:
    print(f"Substances: {', '.join([str(s) for s in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(c) for c in challenges])}")
