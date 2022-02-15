# 2.1 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3) # 8
print(2*8) # 16
print(3*(3+1)) # 12



# 2.2 문자열 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*10)



# 2.3 boolean 자료형 = 참과 거짓을 의미
print(5 > 10) # False
print(5 < 10) # True
print(True) # True
print(False) # False
print(not True) # not은 뒤에 있는 무언가의 반대를 의미, False
print(not False) # True
print(not (5 > 10)) # Fasle의 반대, True



# 2.4 변수
# 애완동물을 소개해 주세요~
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3


print("우리집" + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 " , age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))



# 2.5 주석 = 프로그램 코드 내에는 포함되어 있지만 실제로는 실행되지 않는 문장
'''이렇게
하면
여러문장이
주석처리
됩니다'''

# print("우리집" + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# print(name, "는 " , age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))



# 2장 퀴즈
'''
Quiz) 변수를 이용하여 다음 문장을 출력하시오

변수명
: station

변수값
: "사당", "신도림", "인천공항" 순서대로 입력

출력 문장
: XX 행 열차가 들어오고 있습니다.
'''

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")