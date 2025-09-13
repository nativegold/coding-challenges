import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())

family_relation_dict = {pn : [] for pn in range(1, n + 1)}

m = int(input())

for _ in range(m):
    parent, kid = map(int, input().split())
    family_relation_dict[parent].append(kid)
    family_relation_dict[kid].append(parent)

queue = deque([p1])
visited = [-1] * (n + 1)
visited[p1] = 0

while queue:
    now = queue.popleft()
    for next in family_relation_dict[now]:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            queue.append(next)

print(visited[p2])