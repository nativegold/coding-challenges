count_0: int = 0
count_1: int = 0

T = int(input())
fibo: list[int] = [0] * T

count_dict: dict[int, (int, int)] = {0: (1, 0), 1: (0, 1)}
max_n = 1

for _ in range(T):
    N: int = int(input())

    if N in count_dict:
        print(f"{count_dict[N][0]} {count_dict[N][1]}")
        continue

    for n in range(max_n + 1, N + 1):
        count_dict[n] = (count_dict[n - 2][0] + count_dict[n - 1][0], count_dict[n - 2][1] + count_dict[n - 1][1])

    print(f"{count_dict[N][0]} {count_dict[N][1]}")