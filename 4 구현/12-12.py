# 기둥과 보 설치

pillar = [[]]
bo = [[]]


def checkPillar(x, y):
    if y == 0 or pillar[x][y - 1]:  # 바닥인 경우, 아래에 기둥이 있는경우
        return True
    if (x > 0 and bo[x - 1][y]) or bo[x][y]:  # 보가 있는경우
        return True
    return False


def checkBo(x, y):
    if pillar[x][y - 1] or pillar[x + 1][y - 1]:  # 바로 밑에 기둥이 있는 경우
        return True
    if x > 0 and bo[x - 1][y] and bo[x + 1][y]:  # 양쪽에 보가 있는 경우
        return True
    return False


def canDelete(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y, y + 2):
            if pillar[i][j] and checkPillar(i, j) == False:
                return False
            if bo[i][j] and checkBo(i, j) == False:
                return False
    return True


def solution(n, build_frame):
    global pillar, bo
    pillar = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    bo = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    for x, y, kind, cmd in build_frame:
        if kind == 0:  # 기둥
            if cmd == 1:  # 설치
                if checkPillar(x, y):  # checkPillar가 True인 경우 설치
                    pillar[x][y] = 1
            else:  # 삭제
                pillar[x][y] = 0
                if not canDelete(x, y):  # canDelete가 False 반환시(삭제 못할 경우)
                    pillar[x][y] = 1
        else:  # 보
            if cmd == 1:  # 설치
                if checkBo(x, y):  # checkBo가 True인 경우 설치
                    bo[x][y] = 1
            else:  # 삭제
                bo[x][y] = 0
                if not canDelete(x, y):
                    bo[x][y] = 1

    answer = []
    for i in range(n + 1):
        for j in range(n + 1):
            if pillar[i][j]:
                answer.append([i, j, 0])
            if bo[i][j]:
                answer.append([i, j, 1])

    return answer