import sys

m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    data = sys.stdin.readline().split()
    if len(data) == 1:
        operator = data[0]
    else:
        operator = data[0]
        x = int(data[1]) - 1
    if operator == 'add':
        s |= (1 << x)
    elif operator == 'remove':
        s &= ~(1 << x)
    elif operator == 'check':
        if (s & (1 << x)) != 0:
            print(1)
        else:
            print(0)
    elif operator == 'toggle':
        s ^= (1 << x)
    elif operator == 'all':
        s = (1 << 20) - 1
    elif operator == 'empty':
        s = 0
