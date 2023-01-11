@app.route("/generate_user")
# def userGenerate(): # 유저 랜덤 생성 후 생성된 유저 보여주기
#     conn = mysql.connect()
#     cursor = conn.cursor()
#     if(request.method == "POST"):
#       name = request.form['name']
#       age = request.form['age']
#       cursor.execute(
#         f"""
#         INSERT INTO user(name, age);
#         VALUES('{name}', '{age}');
#         """
#       )
#       conn.commit()
#       cursor.close()
#       conn.close()
#     return jsonify (
#       f"<p>Hello, User!</p>"
#     )
