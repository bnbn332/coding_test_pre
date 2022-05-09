# 볼링공 고르기(이중 for문)

# 볼링공 개수 n과 최대무게 m 공백 입력
n, m = map(int, input().split())
# 각 볼링공 무게 k 공백 입력
weight = list(map(int, input().split()))
# 정렬
weight.sort()

count = 0

for i in range(0, len(weight) - 1):
    for j in range(i, len(weight)):
        if weight[i] != weight[j]:
            count += 1

print(count)
