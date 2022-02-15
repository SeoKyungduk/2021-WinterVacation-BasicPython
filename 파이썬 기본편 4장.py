# 4.1 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)



# 4.2 슬라이싱
jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 부터 2 직전까지 (0, 1)
print("월 : " + jumin[2:4]) # 2 부터 4 직전까지 (2, 3)
print("일 : " + jumin[4:6]) # 4 부터 6 직전까지 (4, 5)

print("생년월일 : " + jumin[0:6]) # 0 부터 6 직전까지 (0, 5)
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지

print("뒤 7자리 : " + jumin[7:14]) # 7 부터 14 직전까지 (7, 13)
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지

# 맨 뒤에서 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])



# 4.3 문자열 처리 함수
python = "Python is Amazing"
# lower 함수는 입력한 문자열 모두를 소문자로 출력함
print(python.lower())

# upper 함수는 입력한 문자열 모두를 대문자로 출력함
print(python.upper())
print(python[0].isupper()) # [0]번째 문자가 대문자인가? = True
print(python[0].islower()) # [0]번째 문자가 소문자인가? = False

# len 함수는 입력한 문자열의 길이를 출력함
print(len(python)) # 17

# replace 함수는 입력한 문자열을 다른 문자열로 바꿔서 출력함
print(python.replace("Python", "Java"))

# index 함수는 문자열에 있는 문자의 위치를 알려줌
location = python.index("n") # "n"의 위치 = 5
print(location)
location = python.index("n", location + 1) # 다음 "n"의 위치 = 15
print(location)

# find 함수도 index 함수와 마찬가지로 문자열에 있는 문자의 위치를 알려줌
print(python.find("n")) # 5
print(python.find("Java")) # find 함수의 경우 원하는 값이 변수에 포함되지 않았을 경우 -1을 출력함
# print(python.index("Java")) # index 함수의 경우 원하는 값이 변수에 포함되지 않았을 경우 에러가 발생함

# count 함수는 원하는 값을 넣었을 때 원하는 값이 문자열에 몇 개 포함되는지 알려줌
print(python.count("n")) # 2



# 4.4 문자열 포맷
# print("a" + "b")
# print("a", "b")

# 방법 1
# %d는 정수값을 의미함
print("나는 %d살입니다." % 20)

# %s는 문자열을 의미함
print("나는 %s을 좋아해요." % "파이썬")

# %c는 캐릭터라서 한 글자를 받음
print("Apple 은 %c로 시작해요." % "A")

# %s를 사용하면 모든 것을 받아서 값을 출력할 수 있음
print("나는 %s살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %s로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))


# 방법 4 (v3.6 이상 ~ )
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")



# 4.5 탈출문자
# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \ 만 출력
print("C:\\Users\\서경덕\\OneDrive\\바탕 화면\\PythonWorkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") # Red 라는 글자를 Pine으로 바뀜

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Pine\tApple")



# 4장 퀴즈
'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀번호 : nav51!
'''

Url = "http://naver.com"
NewUrl = Url.replace("http://", "")
NewUrl2 = NewUrl.replace(".com", "")

print("생성된 비밀번호 : " + NewUrl2[0:3] + str(len(NewUrl2)) + str(NewUrl2.count("e")) + "!")