n = int(input())


def get_next_permutations(data):
    for i in range(n - 1, 0, -1):
        if data[i - 1] < data[i]:
            a = i - 1
            break
    else:
        return False

    for i in range(n - 1, 0, -1):
        if data[a] < data[i]:
            b = i
            break

    data[a], data[b] = data[b], data[a]
    return data[:a + 1] + sorted(data[a + 1:])


data = [i for i in range(1, n + 1)]
while True:
    print(*data)
    data = get_next_permutations(data)
    if not data:
        break
