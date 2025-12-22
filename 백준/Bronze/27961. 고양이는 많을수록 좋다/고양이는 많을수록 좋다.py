import sys

input = sys.stdin.readline

N = int(input())

result = 0

if N == 0:
    print(result)
    exit(0)

cats_count = 1
result += 1

while cats_count < N:
    cats_count *= 2
    result += 1

    if cats_count >= N:
        break

print(result)