import math


def expand(pattern, count):
    length = int(math.pow(3, count))
    temp = [[' '] * (length * 3) for _ in range(length * 3)]
    for x in range(0, length * 3, length):
        for y in range(0, length * 3, length):
            if x == length and y == length:
                continue
            for i in range(length):
                for j in range(length):
                    temp[x + i][y + j] = pattern[i][j]
    if count == k - 1:
        return temp
    else:
        return expand(temp, count + 1)


n = int(input())
k = math.log10(n) / math.log10(3)
pattern = expand([['*']], 0)
for i in range(len(pattern)):
    for j in range(len(pattern[0])):
        print(pattern[i][j], end='')
    print()
