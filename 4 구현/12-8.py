# 문자열 재정렬

s = input() # 문자열 s 입력
result = [] # 알파벳 담을 리스트
value = 0   # 숫자합

for i in s:
    # 만약 알파벳이라면
    if i.isalpha():
        result.append(i)
    # 숫자라면
    else:
        value += int(i)

result.sort()

# 숫자가 하나라도 존재하면 맨뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))  # 리스트를 문자열로 변환
