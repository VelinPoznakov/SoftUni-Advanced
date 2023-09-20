# names = [x for x in input().split()]
# n = int(input())
#
# for i in range(n):
#     if len(names) == n - 1:
#         print(f"Last is {''.join(names)}")
#         break
#     else:
#         print(f"Removed {names[ 1]}")
#         names.remove(names[1])
#         continue
#
#
from collections import deque
kids_names = input().split()
n = int(input())

kids_circle = deque(kids_names)

while len(kids_circle) > 1:
    for _ in range(n - 1):
        kids_circle.rotate(-1)
    removed_kid = kids_circle.popleft()
    print(f"Removed {removed_kid}")

last_kid = kids_circle[0]
print(f"Last is {last_kid}")

class Top(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
