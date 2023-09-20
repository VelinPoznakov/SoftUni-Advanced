# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3

nums = tuple(input().split())

count = []
nums_in_dict = {}

for i in nums:
    if i not in nums_in_dict:
        nums_in_dict[i] = nums.count(i)

for e, times in nums_in_dict.items():
    print(f"{float(e):.1f} - {times} times")
