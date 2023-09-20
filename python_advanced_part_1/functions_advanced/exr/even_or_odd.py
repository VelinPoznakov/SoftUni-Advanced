def even_odd(*args):
    command = []
    nums = []
    for el in args:
        if el == 'even' or el == 'odd':
            command.append(el)
        else:
            nums.append(el)

    if command[0] == 'even':
        for num in nums:
            if num % 2 != 0:
                nums.remove(num)
        return nums

    else:
        for num in nums:
            if num % 2 == 0:
                nums.remove(num)
        return nums


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))