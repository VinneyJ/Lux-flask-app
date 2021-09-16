#!/usr/bin/python3
from abc import abstractproperty
from flask import Flask, request, render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

msql = MySQL(app)

#config

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

@app.route("/", methods=['GET', 'POST'])
def post_article():
    
    if request.method == 'POST':
        postsObj = request.form
        title = postsObj["title"]
        content = postsObj["content"]
        
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True )
