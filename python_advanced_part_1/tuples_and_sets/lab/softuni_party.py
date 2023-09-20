n = int(input())

guests = input()
times = 0
guests_list = {}
not_come = []
while guests != 'END':

    if guests not in guests_list:
        guests_list[guests] = 1
    else:
        guests_list[guests] += 1

    guests = input()

for num, count in guests_list.items():
    if count == 1:
        not_come.append(num)

print(len(not_come))
for i in sorted(not_come):
    print(i)



