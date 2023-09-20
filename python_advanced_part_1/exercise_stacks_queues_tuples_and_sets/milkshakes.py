chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = [int(x) for x in input().split(", ")]

counter = 0

for i in chocolates:
    if i < 0:
        chocolates.remove(i)

for i in cups_of_milk:
    if i < 0:
        cups_of_milk.remove(i)

for c in range(len(chocolates)):
    if chocolates[-1] == cups_of_milk[0]:
        chocolates.pop(-1)
        cups_of_milk.pop(0)
        counter += 1

if counter >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(i) for i in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(i) for i in cups_of_milk)}")
else:
    print("Milk: empty")