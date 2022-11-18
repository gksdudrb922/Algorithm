def d(n):
    data = set()
    for i in range(1, n + 1):
        x = i + sum(list(map(int, list(str(i)))))
        if x <= n:
            data.add(x)
    return data


answer = sorted(list(set(range(1, 10001)) - d(10000)))
print('\n'.join(map(str, answer)))
