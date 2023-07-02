from collections import deque

def bfs(graph, start):
    visited = [start]
    queue = deque([start])
    cnt = 0

    while queue:
        v = queue.popleft()

        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
                cnt += 1

    return cnt

def solution(n, wires):
    answer = n
    graph = {}
    
    for i in range(1, n+1):
        graph[i] = []
        
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        answer = min(abs(bfs(graph, v1) - bfs(graph, v2)), answer)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer