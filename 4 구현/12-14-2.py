# 외벽 점검
import math
import itertools

def solution(n, weak, dist):
    weakSize = len(weak)
    weak = weak + [w + n for w in weak]
    minCnt = math.inf
    for start in range(weakSize):
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1 # 친구 수
            pos = start # 시작점
            for i in range(1, weakSize):    # 시작점이 취약 지점부터 시작하므로 1부터시작, 모든 취약지점이 방문 되는지 확인
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt - 1]:
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)
    if minCnt == math.inf:
        return -1
    return minCnt