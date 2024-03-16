from collections import deque

k = int(input())

stack = deque()

for _ in range(k):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(int(n))

print(sum(stack))
