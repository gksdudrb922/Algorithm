n = int(input())
t = [0]
p = [0]
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


def calculate(day, total):
    global answer

    if day == n + 1:
        answer = max(answer, total)
        return
    elif day > n + 1:
        return

    calculate(day + t[day], total + p[day])
    calculate(day + 1, total)


answer = 0
calculate(1, 0)
print(answer)
