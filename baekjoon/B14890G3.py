n, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def count_road(board):
    result = 0
    for i in range(n):
        road = True
        slope = [False] * n
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                continue
            elif board[i][j] + 1 == board[i][j + 1]:
                if j - L + 1 >= 0 and len(set(board[i][j - L + 1:j + 1])) == 1 and True not in slope[j - L + 1:j + 1]:
                    for k in range(j - L + 1, j + 1):
                        slope[k] = True
                    continue
                else:
                    road = False
                    break
            elif board[i][j] == board[i][j + 1] + 1:
                if j + L + 1 <= n and len(set(board[i][j + 1:j + L + 1])) == 1 and True not in slope[j + 1:j + L + 1]:
                    for k in range(j + 1, j + L + 1):
                        slope[k] = True
                    continue
                else:
                    road = False
                    break
            else:
                road = False
                break
        if road:
            result += 1
    return result


print(count_road(board) + count_road(rotate_a_matrix_by_90_degree(board)))
