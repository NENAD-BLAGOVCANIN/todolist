from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'todolist'
 
mysql = MySQL(app)

@app.route('/')
def home():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall() 
    cursor.close()

    print(tasks)

    return render_template('home.html', tasks=tasks)

@app.route('/add-task', methods=['POST'])
def addTask():

    name = request.form.get("name")
    description = request.form.get("description")

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO tasks (name, description) VALUES (%s, %s)", (name, description))
    mysql.connection.commit()
    cursor.close()

    return redirect("/")


app.run(debug=True)