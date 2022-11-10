from collections import deque

t = int(input())
cogwheel = [deque(list(map(int, input()))) for _ in range(t)]
k = int(input())


def turn_left_side(index, direction):
    left = cogwheel[index][6]
    cogwheel[index].rotate(direction)
    if index == 0:
        return
    if cogwheel[index - 1][2] != left:
        turn_left_side(index - 1, -direction)


def turn_right_side(index, direction):
    right = cogwheel[index][2]
    cogwheel[index].rotate(direction)
    if index == t - 1:
        return
    if cogwheel[index + 1][6] != right:
        turn_right_side(index + 1, -direction)


for _ in range(k):
    index, direction = map(int, input().split())
    index -= 1
    if index - 1 >= 0 and cogwheel[index - 1][2] != cogwheel[index][6]:
        turn_left_side(index - 1, -direction)
    if index + 1 < t and cogwheel[index + 1][6] != cogwheel[index][2]:
        turn_right_side(index + 1, -direction)
    cogwheel[index].rotate(direction)

answer = 0
for i in range(t):
    if cogwheel[i][0] == 1:
        answer += 1

print(answer)
