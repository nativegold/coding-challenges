n = int(input())
words_set = set()

for _ in range(n):
    words_set.add(input())

words = sorted(list(words_set))
words_sorted = sorted(words, key=len)

for i in range(len(words_sorted)):
    print(words_sorted[i])