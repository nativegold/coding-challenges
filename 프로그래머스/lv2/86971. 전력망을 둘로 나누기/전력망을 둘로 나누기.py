from collections import deque

def bfs(graph, start):
    visited = [start]   # 방문한 정점
    queue = deque([start])  # BFS 구현하는 큐
    cnt = 0     # 정점의 수

    # 큐에 원소가 남아있는 경우
    while queue:
        v = queue.popleft()
        
        # 정점과 연결된 간선 탐색
        for w in graph[v]:
            # 정점과 연결된 정점이 방문되지 않았을 경우
            if w not in visited:
                visited.append(w)
                queue.append(w)
                cnt += 1

    return cnt

def solution(n, wires):
    # 송전탑 개수의 차이
    answer = n
    # 그래프(딕셔너리)
    graph = {}  
    
    # 그래프 초기화
    for i in range(1, n+1):
        graph[i] = []
    
    # 간선 추가
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 간선 지우는 경우에 따라 BFS로 탐색하여 최솟값 찾기
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        answer = min(abs(bfs(graph, v1) - bfs(graph, v2)), answer)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer