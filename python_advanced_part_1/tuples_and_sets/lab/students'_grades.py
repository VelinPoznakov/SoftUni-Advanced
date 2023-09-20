# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00

n = int(input())

stack = {}
for i in range(n):
    name, grade = input().split()
    grade = float(grade)
    if name not in stack:
        stack[name] = [grade]
        continue
    stack[name].append(grade)

for name, grade in stack.items():
    print(f"{name} -> {' '.join([str(f'{num:.2f}') for num in grade])} (avg: {(sum(grade) / len(grade)):.2f})")
