# coding=utf-8
#N과 K를 공백으로 입력
n, k = map(int, input().split())

result = 0

while True:
    #n == k로 나누어떨어지는 수 가 될 때까지 1씩 빼기
    target = (n//k)*k   #n이 k로 나누어 떨어지지 않을경우 나누어지는 수 중 가장 가까운 n을 target으로
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더이상 나눌 수 없을 때) 반목문 탈출
    if n<k:
        break
    #k로 나누기
    result += 1
    n //= k

result += (n-1)
print(result)
