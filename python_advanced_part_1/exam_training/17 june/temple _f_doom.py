from collections import deque

tools = deque(int(x) for x in input().split())  # first
substances = [int(x) for x in input().split()]  # last
challenges = [int(x) for x in input().split()]
# t * s remove them if t*s == any of c remove it
# if not t += 1 move it to the back s -= 1 add it again if the s is == 0 not add it

while tools and substances and challenges:
    t = tools.popleft()
    s = substances[-1]

    if t * s in challenges:
        challenges.remove(t * s)

    else:
        tools.append(t + 1)
        if substances[-1] - 1 == 0:
            substances.remove(s)
        else:
            substances[-1] -= 1

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")

else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")


if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")
if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(c) for c in challenges)}")

