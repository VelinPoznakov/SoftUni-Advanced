stack = []
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == '1':
        stack.append(int(command[1]))
    elif stack:
        if command[0] == '2':
            stack.pop()
        elif command[0] == '3':
            print(max(stack))
        else:
            print(min(stack))


while stack:
    print(stack.pop(), end="")
    if stack:
        print(", ", end="")


