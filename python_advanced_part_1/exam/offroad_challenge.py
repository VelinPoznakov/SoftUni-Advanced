from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumpsion = deque([int(x) for x in input().split()])
fuel_needed = deque([int(x) for x in input().split()])

altitude = 0

reached_altitudes = []

while initial_fuel and consumpsion and fuel_needed:
    fuel_quantuty = initial_fuel.pop(-1)
    current_consm = consumpsion.popleft()
    result = fuel_quantuty - current_consm
    i = fuel_needed.popleft()

    if result >= i:
        print(f"John did not reach: Altitude {altitude + 1}")
        break
    else:
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        reached_altitudes.append(f'Altitude {altitude}')
        
if fuel_needed and altitude > 0:
    print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitudes)}")
elif altitude == 0:
    print(f"John failed to reach the top.\nJohn didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")
