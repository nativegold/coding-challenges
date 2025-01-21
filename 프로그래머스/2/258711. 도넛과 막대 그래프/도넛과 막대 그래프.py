from collections import deque

def solution(edges):
    answer = [0, 0, 0, 0]
    graph = {}
    node_edge_count = {}
    
    # index 0: 다른 정점으로 향하는 간선의 수, index 1: 다른 정점에서 들어오는 간선의 수
    for x1, x2 in edges:
        if x1 not in node_edge_count:
            node_edge_count[x1] = [0, 0]
        if x2 not in node_edge_count:
            node_edge_count[x2] = [0, 0]
        
        node_edge_count[x1][0] += 1
        node_edge_count[x2][1] += 1
        
        if x1 not in graph:
            graph[x1] = set()
        graph[x1].add(x2)
    
    generated_node = 0   # 그래프끼리 연결하기 위해 생성한 정점
    
    for node, edge_count in node_edge_count.items():
        if edge_count[0] >= 2 and edge_count[1] == 0:
            generated_node = node
            break
    
    answer[0] = generated_node
    
    visited = set()     # 방문한 노드

    for first_node in graph[generated_node]:    # 생성한 정점이 연결한 그래프의 첫번째 노드들
        if first_node not in graph:
            answer[2] += 1
            continue
            
        if first_node in graph[first_node]:
            answer[1] += 1
            continue
        
        queue = deque(graph[first_node])
            
        has_two_edges = False   # 다른 정점으로 향하는 2개의 간선 이상을 가지고 있는 경우
        has_edge_from_node = False
        
        while queue:    # BFS
            current_node = queue.popleft()
            visited.add(current_node)
            
            if current_node not in graph:
                break
                
            if len(graph[current_node]) >= 2:   # 한 정점이 간선 두 개를 가지고 있는 경우 --> 8자 모양 그래프
                has_two_edges = True
                break
            
            for next_node in graph[current_node]:
                if next_node == first_node:
                    has_edge_from_node = True
                if next_node not in visited:
                    queue.append(next_node)

        if has_two_edges:   # 8자 모양 그래프
            answer[3] += 1
        elif has_edge_from_node:     # 도넛 모양 그래프
            answer[1] += 1
        elif not has_edge_from_node:     # 막대 모양 그래프
            answer[2] += 1

    return answer