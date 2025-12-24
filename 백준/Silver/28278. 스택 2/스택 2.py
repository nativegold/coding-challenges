import sys


input = sys.stdin.readline


N = int(input())


class Stack:
    def __init__(self):
        self._stack = []

    def put(self, X):
        self._stack.append(X)

    def pop(self):
        if not self._stack:
            return -1

        return self._stack.pop()

    def count(self):
        return len(self._stack)

    def is_empty(self):
        return 1 if len(self._stack) == 0 else 0

    def peak(self):
        if not self._stack:
            return -1

        return self._stack[-1]


stack = Stack()

for _ in range(N):
    command = list(map(int, input().split()))
    if command[0] == 1:
        stack.put(command[1])
    elif command[0] == 2:
        print(stack.pop())
    elif command[0] == 3:
        print(stack.count())
    elif command[0] == 4:
        print(stack.is_empty())
    elif command[0] == 5:
        print(stack.peak())
