# 모험가 길드

# 모험가 수
n = int(input())
# 공포도
data = list(map(int, input().split()))
data.sort()


result = 0  # 그룹수
count = 0   # 현재 그룹에 포함된 모험가 수


for i in data:  # 공포도가 낮은것 부터 하나씩 확인하며
    count += 1  # 현재 그룹에 해당 모험가 포함
    if count >= i:  # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이라면, 그룹 결성
        result += 1
        count = 0   # 모험가 수 초기화

print(result)

