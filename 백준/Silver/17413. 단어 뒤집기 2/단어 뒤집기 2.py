from collections import deque

deq = deque()

S = input()
result = str()

is_tag = False

for c in S:
    if is_tag == False and c == ' ':
        while deq:
            result += deq.pop()
        result += ' '
        continue

    if c == '<':
        is_tag = True
        while deq:
            result += deq.pop()
        result += '<'
        continue

    if c == '>':
        is_tag = False
        while deq:
            result += deq.popleft()
        result += '>'
        continue

    deq.append(c)

while deq:
    result += deq.pop()

print(result)
