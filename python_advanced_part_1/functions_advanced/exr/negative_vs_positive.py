nums = [int(i) for i in input().split()]

positive = []
negative = []

for num in nums:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

print(sum(negative))
print(sum(positive))

if sum(positive) > abs(sum(negative)):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")

