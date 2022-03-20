# coding=utf-8
#N과 K를 공백으로 입력
n, k = map(int, input().split())

result = 0  #실행횟수

#n이 k 이상이라면 k로 계속 나누기
while n>=k:
    #n이 k로 나누어지지 않으면 1씩 빼기
    while n%k != 0:
        n -= 1
        result += 1

while n>1:
    n -= 1
    result += 1

print(result)