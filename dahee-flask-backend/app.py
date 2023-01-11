from flask import Flask
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL
from random import randrange
import random

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'dbmasteruser'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234567890'
app.config['MYSQL_DATABASE_DB'] = 'dbmaster'
app.config['MYSQL_DATABASE_HOST'] = 'ls-18967059a4b4707b5b3d098a9f88d75f76075161.cdjhriynzga3.ap-northeast-2.rds.amazonaws.com'

mysql.init_app(app)

@app.route('/generate-user')
def userGenerate(): # 유저 랜덤 생성 후 생성된 유저 보여주기

    # 유저 생성 코드
    password_list = []
    name_list = []
    gender_list = []
    birthday_list = []
    age_list = []
    company_list = []

    for i in range(10):    
        last_name = ["김", "조", "박", "황", "이", "정"] # 성
        first_name = ["희", "영", "수", "건", "민", "은", "섭", "오", "인", "지", "사", "모", "태", "랑", "윤", "설", "호"] # 마지막 글자
        name = str(random.choice(last_name)) + str(random.choice(first_name)) + str(random.choice(first_name))
        
        password = randrange(1000, 9999, 1) # 1000부터 9999까지 차이 1로 4자리 숫자 랜덤
        gender = random.choice(["male", "female"])
        birthday = randrange(600000, 999999, 1)
        age = randrange(1, 100, 1)
        company = random.choice(["samsung", "lg", "hyundai"])
        
        password_list.append(password)
        name_list.append(name)
        gender_list.append(gender)
        birthday_list.append(birthday)
        age_list.append(age)
        company_list.append(company)

    # db코드 
    conn = mysql.connect()
    cursor = conn.cursor() 
    
    # user라는 테이블에 () 안에 있는거 넣음
    for i in range(10):
        cursor.execute(
            f"""
                INSERT INTO user(password, name, gender, birthday, age, company)
                VALUES ('{password_list[i]}','{name_list[i]}','{gender_list[i]}','{birthday_list[i]}',{age_list[i]},'{company_list[i]}');
            """
        )
        conn.commit()
        
    cursor.close()
    conn.close()
    return jsonify({'result':"success"})