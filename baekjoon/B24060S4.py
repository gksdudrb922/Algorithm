def merge_sort(a, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)


def merge(a, p, q, r):
    global count, answer
    i = p
    j = q + 1
    t = 0
    temp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if a[i] <= a[j]:
            temp[t] = a[i]
            i += 1
        else:
            temp[t] = a[j]
            j += 1
        t += 1
    while i <= q:
        temp[t] = a[i]
        i += 1
        t += 1
    while j <= r:
        temp[t] = a[j]
        j += 1
        t += 1
    i = p
    t = 0
    while i <= r:
        count += 1
        if count == k:
            answer = temp[t]
        a[i] = temp[t]
        i += 1
        t += 1


n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
answer = -1
merge_sort(a, 0, n - 1)

print(answer)
