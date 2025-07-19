n = int(input())
sticks = list(map(int, input().split()))
sticks.sort(reverse=True)

lengths = []
i = 0
while i < n - 1:
    if sticks[i] == sticks[i + 1]:
        lengths.append(sticks[i])
        i += 2
    elif sticks[i] - 1 == sticks[i + 1]:
        lengths.append(sticks[i + 1])
        i += 2
    else:
        i += 1

area = 0
for i in range(0, len(lengths) - 1, 2):
    area += lengths[i] * lengths[i + 1]

print(area)