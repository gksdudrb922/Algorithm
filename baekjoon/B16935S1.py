N, M, R = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
operator = list(map(int, input().split()))


def operate_one(data):
    return data[::-1]


def operate_two(data):
    n = len(data)
    for i in range(n):
        data[i] = data[i][::-1]
    return data


def operate_three(data):
    n = len(data)
    m = len(data[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = data[i][j]
    return result


def operate_four(data):
    n = len(data)
    m = len(data[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[m - j - 1][i] = a[i][j]
    return result


def operate_five(data):
    n = len(data)
    m = len(data[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            n_prime = n // 2
            m_prime = m // 2
            x = data[i][j]
            if i < n_prime and j < m_prime:
                result[i][j + m_prime] = x
            elif i < n_prime and j >= m_prime:
                result[i + n_prime][j] = x
            elif i >= n_prime and j >= m_prime:
                result[i][j - m_prime] = x
            else:
                result[i - n_prime][j] = x
    return result


def operate_six(data):
    n = len(data)
    m = len(data[0])
    result = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            n_prime = n // 2
            m_prime = m // 2
            x = data[i][j]
            if i < n_prime and j < m_prime:
                result[i + n_prime][j] = x
            elif i < n_prime and j >= m_prime:
                result[i][j - m_prime] = x
            elif i >= n_prime and j >= m_prime:
                result[i - n_prime][j] = x
            else:
                result[i][j + m_prime] = x
    return result


for op in operator:
    if op == 1:
        a = operate_one(a)
    elif op == 2:
        a = operate_two(a)
    elif op == 3:
        a = operate_three(a)
    elif op == 4:
        a = operate_four(a)
    elif op == 5:
        a = operate_five(a)
    else:
        a = operate_six(a)

for i in range(len(a)):
    for j in range(len(a[0])):
        print(a[i][j], end=' ')
    print()
