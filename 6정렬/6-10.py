#   위에서 아래로

# N입력받기
n = int(input())

# n개의정수 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 정렬
array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')