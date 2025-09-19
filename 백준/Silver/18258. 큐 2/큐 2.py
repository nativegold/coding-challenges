import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push(self, X):
        node = Node(X)
        self._size += 1

        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def pop(self):
        if self._size == 0:
            return -1

        value = self.head.value
        self.head = self.head.next
        self._size -= 1

        if self._size == 0:
            self.tail = None

        return value

    def size(self):
        return self._size

    def empty(self):
        return int(self._size == 0)

    def front(self):
        if self.head is None:
            return -1
        return self.head.value

    def back(self):
        if self.tail is None:
            return -1
        return self.tail.value


input = sys.stdin.readline

N = int(input())
queue = Queue()
results = []

for _ in range(N):
    command = input().split()

    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "front":
        results.append(queue.front())
    elif command[0] == "back":
        results.append(queue.back())
    elif command[0] == "size":
        results.append(queue.size())
    elif command[0] == "empty":
        results.append(queue.empty())
    elif command[0] == "pop":
        results.append(queue.pop())

for result in results:
    print(result)