# 5.1 리스트 [], 순서를 갖는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]

# 순서 뒤집기 가능
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
mix_list = ["조세호", 20, True]
num_list.extend(mix_list)
print(num_list) # [5, 2, 4, 3, 1, '조세호', 20, True]



# 5.2 사전 {}, {key:value}, key에 대한 중복이 안됨
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3]) # "유재석"
print(cabinet[100]) # "김태호"

print(cabinet.get(3)) # "유재석"
# print(cabinet[5]) # 에러발생
print(cabinet.get(5)) # None 출력
print(cabinet.get(5, "사용가능")) # 5라는 key 값에 대한 value 값을 갖고 오는데 없을 경우 "사용가능"을 출력함

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국" # 값을 넣거나 수정
cabinet["C-20"] = "조세호" # 값을 넣거나 수정
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 간 손님
del cabinet["A-3"] # cabinet["A-3"] 값을 삭제함
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐정
cabinet.clear() # 값을 모두 삭제함
print(cabinet)



# 5.3 튜플 (), 리스트와 다르게 내용 변경하거나 추가할 수 없음
menu = ("돈까스", "치즈까스")
print(menu[0]) # "돈까스"
print(menu[1]) # "치즈까스"

# menu.add("생선까스"), 값을 추가할 수 없음
# menu.append("생선가스"), 값을 추가할 수 없음

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩



# 5.4 집합 (set) {}, 중복이 안되고 순서가 없음
my_set = {1, 2, 3, 3, 3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 도 할 수 있거나 python 할 수 있는 개발자)
print(java | python) # {'양세형', '박명수', '김태호', '유재석'}
print(java.union(python)) # {'양세형', '박명수', '김태호', '유재석'}

# 차집합 (java는 할 수 있는데 python 은 할 줄 모르는 개발자)
print(java - python) # {'김태호', '양세형'}
print(java.difference(python)) # {'김태호', '양세형'}

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'유재석', '박명수', '김태호'}

# java 를 잊었어요
java.remove("김태호")
print(java) # {'양세형', '유재석'}



# 5.5 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['주스', '우유', '커피'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('주스', '우유', '커피') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'주스', '우유', '커피'} <class 'set'>



# 5장 퀴즈
'''
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20 이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
-- 축하합니다 --

(활용 예제)
from random import *
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))
'''

# from random import *
# lst = range(1, 21)
# lst = list(lst)
# chicken = lst[0]
# shuffle(lst)
# coffee = lst[1:]
# coffee = (sample(coffee, 3))
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(chicken))
# print("커피 당첨자 : {0}".format(coffee))
# print("-- 축하합니다 --")

from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")