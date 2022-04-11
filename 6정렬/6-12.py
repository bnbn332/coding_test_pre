# 두 배열의 원소 교체

# n과 k 공백으로 입력
n, k = map(int, input().split())

#A의 원소 공백으로 입력
a = list(map(int, input().split()))
#B의 원소 공백으로 입력
b = list(map(int, input().split()))

# A 오름차순 정렬
a.sort()
# B 내림차순
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] , b[i]= b[i], a[i]
    else:
        break

print(sum(a))