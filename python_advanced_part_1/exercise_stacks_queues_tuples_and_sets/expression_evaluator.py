sequence = input().split()
result = 0
for_sums = []
for i in range(len(sequence)):
    for opr in sequence:

        if opr == '*':
            if i == 1:
                result = for_sums[0] * for_sums[1]
                for_sums = []
            else:
                result *= for_sums[0] * for_sums[1]
                for_sums = []

        elif opr == '-':
            if i == 1:
                result = for_sums[0] - for_sums[1]
                for_sums = []
            else:
                result -= for_sums[0] - for_sums[1]
                for_sums = []

        elif opr == '/':
            if i == 1:
                result = for_sums[0] / for_sums[1]
                for_sums = []
            else:
                result /= for_sums[0] / for_sums[1]
                for_sums = []

        elif opr == '+':
            if i == 1:
                result = for_sums[0] + for_sums[1]
                for_sums = []
            else:
                result += for_sums[0] * for_sums[1]
                for_sums = []

        else:
            for_sums.append(int(opr))

