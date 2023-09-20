from collections import deque
quantity_of_food = int(input())
sq = deque([int(x) for x in input().split()])
print(max(sq))
if sum(sq) <= quantity_of_food:
    print("Orders complete")
else:
    while quantity_of_food > 0 and quantity_of_food - sq[0] > 0:
        quantity_of_food -= sq.popleft()

    print("Orders left:", " ".join(str(i) for i in sq))

