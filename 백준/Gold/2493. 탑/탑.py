import sys

input = sys.stdin.readline

N = int(input())
tower_heights = list(map(int, input().split()))

stack = []
answers = []

for i, height in enumerate(tower_heights):
    while stack and stack[-1][1] <= height:
        stack.pop()

    if stack:
        answers.append(stack[-1][0])
    else:
        answers.append(0)

    stack.append((i + 1, height))

print(' '.join(list(map(str, answers))))