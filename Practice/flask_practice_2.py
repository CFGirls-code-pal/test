#November 2016 Deborah Leem for CFG project
#Flask DB
 
from flask import Flask
from flask import render_template
from flask import request
from flask import g
import sqlite3
 
app = Flask("MyApp")
 
def connect_db():
    db = sqlite3.connect("CFG_DB")
    db.row_factory = sqlite3.Row
    return db
 
@app.before_request
def before_request():
    g.db = connect_db()
 
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
 
@app.route("/")
def hello():
   users = g.db.execute('select name, email, language from users order by name').fetchall()
   return render_template("hello.html", users=users)
 
@app.route("/signup", methods=['GET'])
def hello_again():
    return "This is the get method being called"
 
@app.route("/signup", methods=['POST'])
def sign_up():
    form_data = request.form
    with g.db:
        g.db.execute(
            "insert into users (name, email, language) values (?,?,?)",
            (form_data['name'], form_data['email'], form_data['language'])
        )
    return "All OK"
 
app.run()