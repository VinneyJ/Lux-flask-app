#!/usr/bin/python3
from flask import Flask, request, render_template, redirect
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)



#config
db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route("/", methods=['GET', 'POST'])
def post_article():
    
    if request.method == 'POST':
        postsObj = request.form
        title = postsObj["title"]
        content = postsObj["content"]
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO posts (title, post) VALUES (%s, %s)", (title, content))
        mysql.connection.commit()
        cur.close()
        return redirect('/posts')
    return render_template("index.html")

@app.route('/posts')
def get_posts():
    cur = mysql.connection.cursor()
    title_content = cur.execute("SELECT * FROM posts ORDER BY id DESC")
    if title_content > 0:
        posts = cur.fetchall()

        return render_template("posts.html", posts=posts)    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True )
