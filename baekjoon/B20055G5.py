import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
a = deque(list(map(int, input().split())))
robot = deque([False] * n)

answer = 0
while True:
    answer += 1
    a.appendleft(a.pop())
    robot.appendleft(robot.pop())
    robot[-1] = False
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and a[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            a[i + 1] -= 1
    robot[-1] = False
    if a[0] > 0:
        robot[0] = True
        a[0] -= 1
    if a.count(0) >= k:
        break

print(answer)
