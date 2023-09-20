def multiply(*args):
    result = 1
    for n in args:
        result *= n

    return result


print(multiply(1, 4, 5))
