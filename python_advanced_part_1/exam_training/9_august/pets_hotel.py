def accommodate_new_pets(av_hotel_capacity, max_weight_limit, *args):
    for type_pet, weight in args:
        if weight <= max_weight_limit and av_hotel_capacity > 0:
            if type_pet in pets_count:
                pets_count[type_pet] += 1

            else:
                pets_count[type_pet] = 1
            av_hotel_capacity -= 1
        elif weight > max_weight_limit:
            continue
        else:
            print("You did not manage to accommodate all pets!")
            break

    if av_hotel_capacity > 0:
        print(f"All pets are accommodated! Available capacity: {av_hotel_capacity}.")

    sorted_dict = sorted(pets_count.items(), key=lambda x: x[0])
    res = '  Accommodated pets:\n'

    for item in sorted_dict:
        res += f'  {item[0]}: {item[1]}\n'
    return res


pets_count = {}

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))


