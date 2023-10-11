rows, cols = [int(x) for x in input().split()]

start_index = ord("a")

for r in range(rows):
    for c in range(cols):
        print(f"{chr(start_index + r)}{chr(start_index + c + r)}{chr(start_index + r)}", end=' ')

    print()
