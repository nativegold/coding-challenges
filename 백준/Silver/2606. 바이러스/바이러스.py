from collections import deque

computer_count = int(input())
line_count = int(input())

network = {n: [] for n in range(1, computer_count + 1)}

for _ in range(line_count):
    x1, x2 = map(int, input().split())
    network[x1].append(x2)
    network[x2].append(x1)

visited = set()
queue = deque([1])
infected_computer_count = 0

while queue:
    node = queue.popleft()

    if node in visited:
        continue

    visited.add(node)
    infected_computer_count += 1

    for connected_node in network[node]:
        if connected_node not in visited:
            queue.append(connected_node)

print(infected_computer_count - 1)
