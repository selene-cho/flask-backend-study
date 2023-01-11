from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World</h1>"
  
@app.route("/project")
def show_project():
    return "<h1>This is project page</h1>"

@app.route("/about") # url 주소
def show_about():
    return "<h1>This is about page</h1>"
  
# HTML 쿼리
# 특정 게시물을 보여주는 URL
# @app.route("/feeds/<int:feed_id>")
# def show_one_feed(feed_id):
#     return f"<h1>Feed ID : {feed_id}</h1>" 
    # {매개변수}넣는 경우 맨앞에 f"~" 붙여서 문자열로 받아와

@app.route("/<name>")
def hello_name(name):
    return f"Hello, {name}!"

@app.route("/myinfo/<username>")
def show_my_info(username):
    return f"<h1>Username is {username}</h1>"


# REST API 만들기
from flask import request # 유저가 보낸 데이터가 request에 담겨서 온다.
from flask import jsonify # 객체를 유저가 이해할 수 있는 문자열로 만들기위해 json으로! (서버에서 유저에게 데이터를 보내기 위해 사용)
# django에서는 view에 class만들고 get, post...

# GET api/v1/feeds => 피드 조회
# POST api/v1/feeds => 피드 생성
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    # json 데이터 직접 만드는 경우
    data = { 
        "id" : 1,
        "title" : "제목",
        "img" : "www.image.com/1",
        "like" : "100",
        "reviews": [
            {"id":1, "nickname":"hee", "content":"댓글1"},
            {"id":2, "nickname":"hee2", "content":"댓글2"},
            {"id":3, "nickname":"hee3", "content":"댓글3"},
            {"id":4, "nickname":"hee4", "content":"댓글4"},
            {"id":5, "nickname":"hee5", "content":"댓글5"},
        ]
    }
    print(type(data)) # 서버에서 만든 객체 데이터
    print(type(jsonify(data))) # 클라이언트가 이해 할 수 있는 데이터 / type을 json으로 바꿔줘야 사용자가 이해가능
    
    return jsonify(data)

# 게시글 하나 조회
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)
    return jsonify({"result":"success"})

# 게시글 생성
# POST /api/v1/feeds

@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']
    age = request.form['age']
    
    print(name, age)
    return jsonify({'result':'success'})

# DB 커넥트
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'ozdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# conn = mysql.connect()
# cursor = conn.cursor() # 쿼리를 실행하기 위해 필요함
# cursor.execute( # 실행할 쿼리문
#     """
#     SELECT * FROM ozdb;
#     """
# )

# datas = cursor.fetchone() # django -> get()
# datas = cursor.fetchall() # django -> all()

# conn.commit() # commit 하면 데이터가 들어옴
# cursor.close()
# conn.close()


# 유저 부분
@app.route('/api/v1/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    conn = mysql.connect()
    cursor = conn.cursor()   
    if(request.method == "GET"): # 유저 조회
        cursor.execute(
            """
            SELECT * FROM user;
            """
        )
        results = cursor.fetchall()
        return jsonify({"result":results})
    
    elif(request.method == "POST"): # 유저 생성
        name = request.form['name']
        age = request.form['age']
        cursor.execute(
            f"""
            INSERT INTO user(name, age);
            VALUES('{name}','{age}');
            """
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'result':'success'})
    
    # elif(request.method == "PUT"): # 유저 업데이트
    #     cursor.execute(
    #     """
    #     UPDATE;
    #     """
    #     )
    #     return
    #
    # elif(request.method == "DELETE"): # 유저 삭제
    #     cursor.execute(
    #     """
    #     DELETE;
    #     """
    #     )
    #     returns