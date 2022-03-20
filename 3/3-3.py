# coding=utf-8

#행의 개수 N과 열의 개수 M을 공백을 기준으로 입력
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    #현재 행 중 가장 작은수 찾기
    min_value = min(data)
    #그중 가장 큰 수 찾기
    result = max(result, min_value)

print(result)