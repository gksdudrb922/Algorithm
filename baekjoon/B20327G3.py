import sys


def operate_one(L):
    temp = [[a[i][j] for j in range(N)] for i in range(N)]
    count = 0
    for x in range(0, N, L):
        for y in range(0, N, L):
            for i in range(x, x + L):
                for j in range(y, y + L):
                    a[x + L - 1 - i + (L * count)][j] = temp[i][j]
        count += 1


def operate_two(L):
    temp = [[a[i][j] for j in range(N)] for i in range(N)]
    count = 0
    for x in range(0, N, L):
        for y in range(0, N, L):
            for i in range(x, x + L):
                for j in range(y, y + L):
                    a[i][y + L - 1 - j + (L * count)] = temp[i][j]
            count += 1
        count = 0


def operate_three(L):
    temp = [[a[i][j] for j in range(N)] for i in range(N)]
    count = 0
    C = 0
    R = 0
    for x in range(0, N, L):
        for y in range(0, N, L):
            for i in range(x, x + L):
                for j in range(y, y + L):
                    a[j - (L * R) + (L * count)][x + L - 1 - i + (L * C)] = temp[i][j]
            C += 1
            R += 1
        count += 1
        C = 0
        R = 0


def operate_four(L):
    temp = [[a[i][j] for j in range(N)] for i in range(N)]
    count = 0
    C = 0
    R = 0
    for x in range(0, N, L):
        for y in range(0, N, L):
            for i in range(x, x + L):
                for j in range(y, y + L):
                    a[y + L - 1 - j + (L * R)][i + (L * C) - (L * count)] = temp[i][j]
            C += 1
        count += 1
        C = 0
        R += 1


def operate_five(L):
    operate_one(N)
    operate_one(L)


def operate_six(L):
    operate_two(N)
    operate_two(L)


def operate_seven(L):
    operate_three(N)
    operate_four(L)


def operate_eight(L):
    operate_four(N)
    operate_three(L)


input = sys.stdin.readline
n, r = map(int, input().split())
N = 2 ** n
a = [list(map(int, input().split())) for _ in range(N)]
for _ in range(r):
    k, l = map(int, input().split())
    L = 2 ** l
    temp = [[0] * N for _ in range(N)]

    if k == 1:
        operate_one(L)
    elif k == 2:
        operate_two(L)
    elif k == 3:
        operate_three(L)
    elif k == 4:
        operate_four(L)
    elif k == 5:
        operate_five(L)
    elif k == 6:
        operate_six(L)
    elif k == 7:
        operate_seven(L)
    else:
        operate_eight(L)

for i in range(N):
    print(*a[i])

'''
PyPy3에서만 통과
'''