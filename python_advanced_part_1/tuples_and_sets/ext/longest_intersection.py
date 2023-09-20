n = int(input())

num_list = [] # [[0, 3], [1, 2]]
first_set = set()
second_set = set()

for i in range(n):
    nums = input().split('-')
    for num in nums:
        num_list.append(num.split(','))
        map(int(el), (for el in num_list))

        #for every_num in range(num_list[0][0], num)
