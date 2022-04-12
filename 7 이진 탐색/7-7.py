# 부품 찾기 집합 자료형 이용

n = int(input())

# 가게에 있는 전체 부품 번호를 입력받아 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        