n = int(input())

parking = set()

for i in range(n):
    command, car = input().split(", ")

    if command == 'IN':
        parking.add(car)
    elif command == 'OUT':
        parking.remove(car)

if parking:
    for car in parking:
        print(car)
else:
    print('Parking Lot is Empty')  