# 8.1 표준입출력
# sep를 통해서 문장과 문장 사이를 입력한 것으로 나눌 수 있음
print("Python", "Java", sep=",") # Python,Java
print("Python", "Java", "JavaScript", sep=" VS ") # Python VS Java VS JavaScript

# end를 통해서 문장의 끝 부분을 입력한 값으로 문장과 문장을 이을 수 있음
print("Python", "Java", sep=",", end = "?")
print("무엇이 더 재밌을까요?") # Python,Java?무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout) # stdout = 표준출력으로 문장이 찍힘
print("Python", "Java", file=sys.stderr) # stderr = 표준에러로 문장이 찍힘

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    # 총 8칸을 확보한 후 왼쪽으로 정렬
    # 총 4칸을 확보한 후 오른쪽으로 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21): # 1 ~ 20
    print("대기번호 : " + str(num).zfill(3)) # 3 크기만큼을 확보하고 값이 없는 빈 공간은 0으로 채움

# 사용자의 입력을 통해서 값을 받게 되면 항상 문자열(str) 형태로 출력됨   
# answer = input("아무 값이나 입력하세요 : ")
answer = 10
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")



# 8.2 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500)) #        500

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500)) #       +500
print("{0: >+10}".format(-500)) #       -500

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500)) # +500______
print("{0:_<+10}".format(-500)) # -500______

# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(10000000000))

# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(10000000000))
print("{0:+,}".format(-10000000000))

# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니깐 빈 자리는 ^ 로 채워주기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점 특정 자리수 까지만 표시 (소수점 2번째 자리까지 표시, 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))



# 8.3 파일입출력
# "w" = 파일을 쓰기 위한 목적 (덮어쓰기)
# utf8을 사용하지 않으면 한글 파일을 열때 이상한 문자로 열림
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close()

# "a" = 이어서 쓰기
score_file = open("score.txt", "a", encoding="utf")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# "r" = 파일에 있는 내용을 읽어옴
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print()
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
print()
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()



# 8.4 pickle = 프로그램상에서 사용하고 있는 데이터를 파일 형태로 저장하고 pickle을 이용해 파일에 있는 데이터를 사용함
# pickle에서는 바이너리 타입을 사용해야하며, 굳이 인코딩을 사용할 필요가 없음
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile 에 있는 정보를 file 에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb") # 읽기 = "rb"
profile = pickle.load(profile_file) # 파일에 있는 내용을 갖고 와서 데이터 형태로 불러옴, file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()



# 8.5 with = close를 하지 않아도 됨
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())



# 8장 퀴즈
'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 : 
이름 : 
업무 요약 : 

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ... 와 같이 만듭니다.
'''

for i in range(1, 51): # 1 ~ 50
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무 요약 : ")