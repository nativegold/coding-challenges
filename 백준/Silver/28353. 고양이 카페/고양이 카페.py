n, k = map(int, input().split())

cats = sorted(list(map(int, input().split())))

p1 = 0
p2 = len(cats) - 1

result = 0
while p1 < p2:
    two_cats_weight = cats[p1] + cats[p2]

    if two_cats_weight <= k:
        result += 1
        p1 += 1

    p2 -= 1

print(result)
