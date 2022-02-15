# 3.1 연산자
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 2^3 = 8
print(5%3) # 5/3의 나머지 = 2
print(10%3) # 10/3의 나머지 = 1
print(5//3) # 5/3의 몫 = 1
print(10//3) # 10/3의 몫 = 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 <= 3) # False
print(5 <= 5) # True

print(3 == 3) # 3은 3과 똑같은가? = True
print(4 == 2) # 4는 2와 똑같은가? = False
print(3 + 4 == 7) # 3 + 4는 7과 똑같은가? = True

print(1 != 3) # 1과 3은 같지 않은가? = True
print(not (1 != 3)) # True의 반대 = False

print((3 > 0) and (3 < 5)) # 앞의 항과 뒤의 항이 모두 만족 = True
print((3 > 0) & (3 < 5)) # 앞의 항과 뒤의 항이 모두 만족 = True

print((3 > 0) or (3 > 5)) # 앞의 항이나 뒤의 항이 참을 만족 = True
print((3 > 0) | (3 > 5)) # 앞의 항이나 뒤의 항이 참을 만족 = True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False



# 3.2 간단한 수식
print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4
print(number) # 14
number = number + 2
print(number) # 16
number += 2
print(number) # 18
number *= 2
print(number) # 36
number /= 2
print(number) # 18
number -= 2
print(number) # 16

number %= 5
print(number) # 1



# 3.3 숫자처리함수
# abs 함수는 절대값을 출력함
print(abs(-5)) # 5
print(pow(4, 2)) # 4^2 = 4*4 = 16
# max 함수는 입력한 값 중 가장 큰 값을 출력함
print(max(5, 12)) # 12
# min 함수는 입력한 값 중 가장 작은 값을 출력함
print(min(5, 12, 3)) # 3
# round 함수는 입력한 값을 반올림함
print(round(3.14)) # 3
print(round(4.99)) # 5

# math 라이브러리에 있는 모든 것을 이용하겠다는 의미
from math import *
# floor 함수는 입력한 값을 내려 출력함
print(floor(4.99)) # 4
# ceil 함수는 입력한 값을 올려 출력함
print(ceil(3.14)) # 4
# sqrt 함수는 입력한 값의 제곱근 값을 출력함
print(sqrt(16)) # 4



# 3.4 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성
print(int(random() * 10) + 1) # 0 ~ 11 미만의 임의의 값을 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값을 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값을 생성



# 3장 퀴즈
'''
Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

조건1 : 랜덤으로 날짜를 뽑아야 함
조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
조건3 : 매월 1 ~ 3일은 스터디 준비를 해야 하므로 제외

(출력문 예제)
오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
'''
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")