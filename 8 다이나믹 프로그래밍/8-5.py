# x입력받기
x = int(input())

# dp 테이블 초기화
d = [0] * 30001

for i in range(2, x + 1):   # elif안쓰는 이유 if로만 써야 계산을 다거침
    # 1을 뺴는 경우
    d[i] = d[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])