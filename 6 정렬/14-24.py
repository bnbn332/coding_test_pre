# 안테나

n = int(input())    # 집의 수
house = list(map(int, input().split()))
house.sort()

# 중간값 출력
print(house[(n - 1) // 2])