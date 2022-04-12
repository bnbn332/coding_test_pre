# 부품찾기 이진탐색 (반복문)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

# 부품 n개입력
n = int(input())
# 가게에 있는 부품 번호 공백 입력
array = list(map(int, input().split()))
array.sort()    # 이진 탐색 위해 정렬

# 손님 확인 m 입력
m = int(input())
# 손님 확인용 부품 공백 입력
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')