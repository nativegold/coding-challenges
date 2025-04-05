import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

gems = []
for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V))  # (무게, 가격)

gems.sort()

bags = []
for _ in range(K):
    bags.append(int(input()))

bags.sort()

max_heap = []
result = 0
idx = 0

for bag in bags:
    # 현재 가방의 무게 제한을 넘지 않는 모든 보석을 힙에 추가
    while idx < N and gems[idx][0] <= bag:
        heapq.heappush(max_heap, -gems[idx][1])
        idx += 1

    if max_heap:    # 가장 비싼 보석 선택
        result += -heapq.heappop(max_heap)

print(result)