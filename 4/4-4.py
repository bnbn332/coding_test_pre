# coding=utf-8

#첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백 입력 n>=3, m<=50
n, m = map(int, input().split())

#맵을 0으로 초기화
d = [[0]*m for _ in range(n)]

#둘째 줄에 게임 캐릭터가 있는 칸의 좌표 x,y 바라보는 방향 각각 서로 공백으로 구분 입력
x, y, direction = map(int, input().split())

#현재 좌표 방문 처리
d[x][x] = 1

#전체 맵 정보
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1: #0북 1동 2남 3서
        direction = 3

count = 1
turn_time = 0
while True:
    #왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전후 가보지 않은 칸 이라면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    #회전후 가봤거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있는 경우
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다
        else:
            break
        turn_time = 0

print(count)