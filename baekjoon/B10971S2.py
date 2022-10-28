n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]


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


path = [i for i in range(n)]
answer = 1e7
while True:
    cost = 0
    for i in range(n - 1):
        c = w[path[i]][path[i + 1]]
        if c == 0:
            break
        cost += c
    else:
        c = w[path[n - 1]][path[0]]
        if c == 0:
            pass
        else:
            cost += c
            answer = min(answer, cost)
    path = get_next_permutations(path)
    if not path or path[0] != 0:
        break

print(answer)

'''
1. path[0] != 0 -> 이 문제의 핵심
'''