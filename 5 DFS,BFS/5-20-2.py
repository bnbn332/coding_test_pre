# 감시피하기(bfs)

from collections import deque
from itertools import combinations

# S=학생, T=선생님 X=빈공간 O=장애물

n = int(input())    # 복도 크기
board = []          # 복도 정보
teacher = []        # 선생님 위치 정보
spaces = []         # 모든 빈공간 위치 정보

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        if board[i][j] == 'X':
            spaces.append((i, j))


def bfs():   # 학생 찾으면 False 반환
    q = deque(teacher)
    while q:
        x, y = q.popleft()
        for i in range(4):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < 0:
                    if board[nx][ny] == 'X':    # 상하좌우 빈공간이면
                        board[nx][ny] = 'T'
                    elif board[nx][ny] == 'S':  # 상하좌우 학생이 있으면
                        return False
                    elif board[nx][ny] == 'O':  # 상하좌우 장애물이 있으면
                        break
                else:
                    break
    return True


check = False


for data in list(combinations(spaces, 3)):
    for x, y in data:
        board[x][y] = 'O'
    if bfs():
        check = True
        break
    for x, y in data:
        board[x][y] = 'X'

if check:
    print('YES')
else:
    print('NO')