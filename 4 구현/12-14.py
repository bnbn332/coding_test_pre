# 외벽 점검

from itertools import permutations  # 순열 라이브러리

def solution(n, weak, dist):  # n: 외벽 둘레, weak: 취약점 위치 배열, dist: 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열
    # 길이를 2배로 늘려 원형을 일자로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1  # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1 로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1  # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1  # 새친구 투입
                    if count > len(dist):  # 더 투입이 불가능 할 경우
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return - 1

    return answer
