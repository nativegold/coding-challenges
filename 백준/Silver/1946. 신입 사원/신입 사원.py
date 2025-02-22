import sys

t = int(input())

for _ in range(t):
    n = int(input())
    applicants = []

    for _ in range(n):
        applicants.append(tuple(map(int, sys.stdin.readline().split())))

    applicants.sort(key=lambda x: x[0])

    interview_min_ranking = applicants[0][1]

    result = 1
    for i in range(1, n):
        if applicants[i][1] > interview_min_ranking:
            continue

        interview_min_ranking = applicants[i][1]
        result += 1

    print(result)
