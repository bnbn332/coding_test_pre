n = int(input())
coins = list(map(int, input().split()))

# 정렬
coins.sort()
# 타겟값 = 1
target = 1

for i in coins:
    if target < i:
        # 만들 수 없을경우 종료
        break
    target += i

print(target)
