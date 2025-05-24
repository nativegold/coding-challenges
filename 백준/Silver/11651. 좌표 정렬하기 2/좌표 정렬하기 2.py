import sys

input = sys.stdin.readline

N = int(input())
dots = []

for _ in range(N):
    dots.append(list(map(int, input().split())))

dots.sort(key=lambda x: (x[1], x[0]))

for dot in dots:
    print(f"{dot[0]} {dot[1]}")