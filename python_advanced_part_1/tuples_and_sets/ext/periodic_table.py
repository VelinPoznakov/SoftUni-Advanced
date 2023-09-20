m = int(input())

set_of_elements = set()

for i in range(m):
    element = input().split()
    for el in element:
        set_of_elements.add(el)

print(*set_of_elements, sep='\n')