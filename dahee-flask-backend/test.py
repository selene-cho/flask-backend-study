from random import randrange
import random

# 이름 랜덤하게 3자리 만들기
last_name = ["김", "조", "박", "황", "이", "정"] # 성
first_name = ["희", "영", "수", "건", "민", "은", "섭", "오", "인", "지", "사", "모", "태", "랑", "윤", "설", "호" ] # 마지막 글자

name = str(random.choice(last_name)) + str(random.choice(first_name)) + str(random.choice(first_name))
print(name)

# 비밀번호
password = randrange(1000,9999,1) # 1000부터 9999까지 차이 1로 4자리 숫자 랜덤
print(password)
#성별
gender = random.choice(["male", "female"])
print(gender)
#생일
birthday = randrange(600000, 999999, 1)
print(birthday)
#나이
age = randrange(1, 100, 1)
print(age)
#회사
company = random.choice(["samsung", "lg", "hyundai"])
print(company)