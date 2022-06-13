# 국영수

n = int(input())    # 학생수
students = []   # 학생 정보를 담을 리스트

for _ in range(n):
    students.append(input().split())


# 이름 국 영 수
# 1) 국어 감소
# 2) 국어 같으면, 영어 증가
# 3) 국어 영어 같으면, 수학 감소
# 4) 다 같으면, 이름 사전순 증가

students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# 정렬 된 상태에서 이름만 N줄에 걸쳐 출력
for student in students:
    print(student[0])