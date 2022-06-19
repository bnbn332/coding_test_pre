# 퇴사

# 점화식 = dp[i] = max(p[i] + dp[i + t[i]], max_value)

n = int(input())
t = []  # 각 상담을 완료하는 데 걸리는 시간
p = []  # 각 상담을 완료했을 때 받는 금액
dp = [0] * (n + 1)  # dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):  #(시작, 끝, 증가폭)
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(p[i] + dp[i + t[i]], max_value)
        max_value = dp[i]
    # 상담 기간이 벗어나는 경우
    else:
        dp[i] = max_value


print(max_value)