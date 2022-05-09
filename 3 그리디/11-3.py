# 문자열 뒤집기

s = input()
count0 = 0  # 0으로 바꾸는 경우 횟수
count1 = 0  # 1로 바꾸는 경우 횟수

# 첫번쨰 원소 확인
if s[0] == '0':
    count1 += 1
else:
    count0 += 1

for i in range(1, len(s) - 1):  # 두번째 부터 끝까지 확인
    if s[i] != s[i+1]:
        if s[i+1] == '0':
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))