
class ValueCannotBeNegative(Exception):
    pass


for i in range(5):
    value = int(input())
    if value < 0:
        raise ValueCannotBeNegative
