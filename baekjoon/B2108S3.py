from collections import Counter
import sys

input = sys.stdin.readline
n = int(input())
data = [int(input()) for _ in range(n)]
print(int(round(sum(data) / len(data), 0)))
data.sort()
print(data[len(data) // 2])
counter = dict(Counter(data))
max_value = max(counter.values())
max_key = []
for key in counter:
    if counter[key] == max_value:
        max_key.append(key)
if len(max_key) >= 2:
    print(sorted(max_key)[1])
else:
    print(max_key[0])
print(data[-1] - data[0])
