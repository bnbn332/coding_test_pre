# 럭키 스트레이트

# 정수 N 자릿수는 항상 짝수
n = input()
length = len(n)
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# summary가 0이면 왼쪽 오른쪽 합이 같음
if summary == 0:
    print("LUCKY")
else:
    print("READY")

