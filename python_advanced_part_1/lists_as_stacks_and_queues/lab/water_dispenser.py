quantity = int(input())
people_for_water = input()
people_queue = []

while people_for_water != 'Start':
    people_queue.append(people_for_water)
    people_for_water = input()

people_for_water = input()

while people_for_water != 'End':
    command = people_for_water.split()

    if command[0] == 'refill':
        quantity += int(command[1])
    else:
        if int(command[0]) > quantity:
            print(f"{people_queue[0]} must wait")
            people_queue.remove(people_queue[0])

        else:
            print(f"{people_queue[0]} got water")
            people_queue.remove(people_queue[0])
            quantity -= int(command[0])

    people_for_water = input()

if quantity <= 0:
    quantity = 0
    print(f"{quantity} liters left")
else:
    print(f"{quantity} liters left")
