import sys

input = sys.stdin.readline

n, k, t = map(int, input().split())
sharks = list(map(int, input().split()))
sharks.sort()
bigger_sharks = []

while k > 0 and (sharks or (bigger_sharks and t > bigger_sharks[-1])):

    if bigger_sharks and t > bigger_sharks[-1]:
        sharks.append(bigger_sharks.pop())
    elif sharks:
        shark = sharks.pop()

        if t > shark:
            t += shark
            k -= 1
        else:
            bigger_sharks.append(shark)

print(t)