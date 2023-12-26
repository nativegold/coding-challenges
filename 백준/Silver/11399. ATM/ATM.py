n = int(input())
time_list = list(map(int, input().split()))

time_list.sort()
time_sum = [time_list[0]]

for i in range(1, n):
    time_sum.append(time_sum[i-1] + time_list[i])
        
print(sum(time_sum))