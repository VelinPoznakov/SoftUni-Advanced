n, m = map(int, tuple(input().split()))

n_set = set()
m_set = set()

for nums in range(n):
    n_set.add(nums)

for num in range(m):
    m_set.add(num)

print(n_set.difference(m_set))