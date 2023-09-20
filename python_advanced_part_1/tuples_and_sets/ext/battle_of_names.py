n = int(input())
names = {}
even = set()
odd = set()

for i in range(1, n + 1):
    name = input()
    names[name] = i

ch_sum = 0

for key, value in names.items():
    for ch in key:
        ch_sum += ord(ch)

    ch_sum //= value
    names[key] = ch_sum
    ch_sum = 0

for _, value in names.items():
    if value % 2 == 0:
        even.add(value)
    else:
        odd.add(value)

if sum(odd) == sum(even):
    print(*(even | odd), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=', ')
else:
    print(*even.symmetric_difference(odd), sep=', ')

