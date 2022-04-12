# 부품찾기 계수정렬

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

# 손님 확인 부품 하나씩 확인
for i in x:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')