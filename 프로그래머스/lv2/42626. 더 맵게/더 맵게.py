from heapq import heapify, heappop, heappush

def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    
    while scoville[0] < K and len(scoville) > 1:
        answer += 1
        x1 = heappop(scoville)
        x2 = heappop(scoville)
        heappush(scoville, x1 + x2 * 2)
        
    return answer if scoville[0] >= K else -1