# 편집 거리

# 점화식 : 두문자가 같은경우 왼쪽위 수 삽입 dp[i][j] = dp[i - 1][j - 1]
# 두문자가 다른 경우 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체)에 해당하는 수중 가장 작은 수 + 1 삽입
# dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]

def edit_dist(str1, str2):
    n = len(str1)
    m = len(str2)

    # 2차원 DP테이블 초기화
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 테이블 초기 설정
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j

    # 최소 편집 거리 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 문자가 같다면, 왼쪽 위에 해당하는 수 그대로 삽입
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # 문자가 다르다면, 3가지 중 최솟값 찾기
            else:  # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽위)
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    return dp[n][m]


# 두 문자열을 입력받기
str1 = input()
str2 = input()

# 최소 편집 거리 출력
print(edit_dist(str1, str2))