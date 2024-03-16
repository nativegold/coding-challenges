k = int(input())

stack = []

for _ in range(k):
    n = int(input())

    if n == 0:
        stack.pop()
    else:
        stack.append(int(n))

print(sum(stack))

