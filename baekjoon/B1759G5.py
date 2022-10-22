L, C = map(int, input().split())
data = input().split()


def check(password):
    count = 0
    for v in vowel:
        count += password.count(v)
    if count >= 1 and len(password) - count >= 2:
        return True
    return False


def make_password(index, count, password):
    if count == L:
        if check(password):
            answer.append(password)
        return

    for i in range(index, C):
        make_password(i + 1, count + 1, password + data[i])


answer = []
vowel = ['a', 'e', 'i', 'o', 'u']
data.sort()
make_password(0, 0, "")
print('\n'.join(answer))
