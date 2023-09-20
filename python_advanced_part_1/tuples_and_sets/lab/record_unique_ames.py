num = int(input())

my_set = set()

for _ in range(num):
    name = input()
    my_set.add(name)

for name in my_set:
    print(name)