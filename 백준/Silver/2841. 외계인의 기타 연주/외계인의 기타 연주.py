import sys
from collections import deque

input = sys.stdin.readline

N, P = map(int, input().split())

finger_dict = {}
result = 0

for _ in range(N):
    line, plot = map(int, input().split())

    if line not in finger_dict:
        finger_dict[line] = deque()
        finger_dict[line].append(plot)
        result += 1
        continue

    while finger_dict[line] and finger_dict[line][-1] > plot:
        finger_dict[line].pop()
        result += 1

    if not finger_dict[line] or finger_dict[line][-1] != plot:
        finger_dict[line].append(plot)
        result += 1

print(result)
