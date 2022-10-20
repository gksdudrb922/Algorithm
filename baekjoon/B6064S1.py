import math


def lcd(x, y):
    return (x * y) // math.gcd(x, y)


t = int(input())
answer = []
for _ in range(t):
    m, n, x, y = map(int, input().split())
    LCD = lcd(m, n)
    search = False
    while x <= LCD and y <= LCD:
        if x == y:
            search = True
            answer.append(x)
            break
        else:
            if x < y:
                x += m
            else:
                y += n
    if not search:
        answer.append(-1)

print('\n'.join(map(str, answer)))
