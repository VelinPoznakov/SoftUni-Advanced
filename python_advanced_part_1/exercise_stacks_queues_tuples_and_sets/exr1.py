sq1 = set(int(x) for x in input().split())
sq2 = set(int(x) for x in input().split())

# for _ in range(int(input())):
#     command = input().split()
#     if command[0] == 'Add':
#         if command[1] == 'First':
#             [(sq1.add(int(i))) for i in command[2::]]
#
#         else:
#             [(sq2.add(int(i))) for i in command[2::]]
#
#     elif command[0] == 'Remove':
#         if command[1] == 'First':
#             for i in command[2::]:
#                 if i in sq1:
#                     sq1.remove(i)
#                 else:
#                     continue
#         else:
#             for i in command[2::]:
#                 if i in sq2:
#                     sq2.remove(i)
#                 else:
#                     continue
#
#     else:
#         if sq2.issubset(sq1):
#             print('True')
#         else:
#             print('False')
#
# print(*sorted(sq1), sep=', ')
# print(*sorted(sq2), sep=', ')


for _ in range(int(input())):
    primary, secondary, *nums = input().split()
    nums = [int(num) for num in nums]
    if primary + ' ' + secondary == 'Add First':
        [(sq1.add(int(i))) for i in nums]
    elif primary + ' ' + secondary == 'Add Second':
        [(sq2.add(int(i))) for i in nums]
    elif primary + " " + secondary == "Remove First":
        for i in nums:
            if i in sq1:
                sq1.remove(int(i))
            else:
                continue
    elif primary + " " + secondary == "Remove Second":
        for i in nums:
            if i in sq2:
                sq2.remove(int(i))
            else:
                continue

    else:
        if sq2.issubset(sq1):
            print('True')
        else:
            print('False')

print(*sorted(sq1), sep=', ')
print(*sorted(sq2), sep=', ')
