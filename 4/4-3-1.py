# coding=utf-8

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
result = 0

x = ord(input_data[0]) - 96
y = int(input_data[1])

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx>=1 and nx<=8 and ny>=1 and ny<=8:
        result += 1

print(result)