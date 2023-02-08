from flask import Flask, render_template
from flaskext.mysql import MySQL
import mysql.connector

app = Flask(__name__)
try:
    mysql=MySQL()
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = '@Obama123'
    app.config['MYSQL_DATABASE_DB'] = 'studentmanagement'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()
    print("connection is successful!")

    cursor = conn.cursor()
    sql="insert into student (code,name) values (%s,%s)"
    val=("SV01","Thanh Tran")
    cursor.execute(sql,val)
    conn.commit()
    print(cursor.rowcount," record inserted")

except mysql.connector.Error as e:
    print("Error = ",e)
finally:
    conn.close()
    cursor.close()
    print("Mysql is closed")