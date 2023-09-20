text = input()

count_times = {}

for ch in text:
    if ch not in count_times:
        count_times[ch] = 1
    else:
        count_times[ch] += 1

for el, value in sorted(count_times.items()):
    print(f"{el}: {value} time/s")