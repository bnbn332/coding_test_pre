# 효율적인 화폐 구성

n, m = map(int, input().split())

# n개의 화폐 단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)    # 0원부터 m원까지라 m+1

d[0] = 0

for i in range(n):  # i 화폐단위
    for j in range(array[i], m + 1):    # j 각각 금액
        if d[j - array[i]] != 10001:    # (i - k)원을 만드는 방법이 존재 한다면
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])