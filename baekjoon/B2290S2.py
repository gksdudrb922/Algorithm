s, n = input().split()

s = int(s)
data = list(n)

for num in data:
    if num in ['1', '4']:
        print(' ' * (s + 2), end=' ')
    else:
        print(' ' + '-' * s + ' ', end=' ')
print()

for _ in range(s):
    for num in data:
        if num in ['1', '2', '3', '7']:
            print(' ' * (s + 1) + '|', end=' ')
        elif num in ['5', '6']:
            print('|' + ' ' * (s + 1), end=' ')
        else:
            print('|' + ' ' * s + '|', end=' ')
    print()

for num in data:
    if num in ['1', '7', '0']:
        print(' ' * (s + 2), end=' ')
    else:
        print(' ' + '-' * s + ' ', end=' ')
print()

for _ in range(s):
    for num in data:
        if num in ['1', '3', '4', '5', '7', '9']:
            print(' ' * (s + 1) + '|', end=' ')
        elif num in ['2']:
            print('|' + ' ' * (s + 1), end=' ')
        else:
            print('|' + ' ' * s + '|', end=' ')
    print()

for num in data:
    if num in ['1', '4', '7']:
        print(' ' * (s + 2), end=' ')
    else:
        print(' ' + '-' * s + ' ', end=' ')
print()
