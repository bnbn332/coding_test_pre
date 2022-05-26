# 치킨 배달

from itertools import combinations  # 조합 라이브러리

# N: 도시의 크기 M: 치킨집 수
n, m = map(int, input().split())
chicken, house = [], []

# 0: 빈칸, 1: 집, 2: 치킨집
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))    # 집
        elif data[c] == 2:
            chicken.append((r, c))  # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 수
candidates = list(combinations(chicken, m))


def get_sum(candidates):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집 찾기
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
