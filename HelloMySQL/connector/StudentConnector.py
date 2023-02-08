from flask import Flask
from flaskext.mysql import MySQL

from data.Student import Student

class StudentConnector:
    def __int__(self):
        pass
    def get_list_students(self):
        mysql = MySQL()
        app = Flask(__name__)
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = '@Obama123'
        app.config['MYSQL_DATABASE_DB'] = 'studentmanagement'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)

        conn = mysql.connect()
        print("connection is successful!")

        cursor = conn.cursor()

        cursor.execute("select * from student")
        data = cursor.fetchall()
        students=[]
        for item in data:
            students.append(Student(item[0],item[1],item[2]))
        conn.close()
        cursor.close()
        return students
    def insert_student(self,student):
        mysql = MySQL()
        app = Flask(__name__)
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = '@Obama123'
        app.config['MYSQL_DATABASE_DB'] = 'studentmanagement'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)

        conn = mysql.connect()
        print("connection is successful!")

        cursor = conn.cursor()
        sql = "insert into student (code,name) values (%s,%s)"
        val = (student.Code, student.Name)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        cursor.close()
        return  cursor.rowcount