from collections import deque

N = int(input())

card_deque = deque([n for n in range(1, N+1)])

while len(card_deque) > 1:
    print(card_deque.popleft(), end=' ')
    card_deque.append(card_deque.popleft())

if card_deque:
    print(card_deque.popleft(), end=' ')