n = [x for x in input().split()]

for i in range(len(n)):
    print(n.pop(-1), sep="", end=" ")
