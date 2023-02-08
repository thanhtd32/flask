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

    cursor.execute("select ID,Code,Name from student")
    data = cursor.fetchmany(4)
    print("ID\tCode\tName")
    for item in data:
        print(item[0],"\t",item[1],"\t",item[2])

except mysql.connector.Error as e:
    print("Error = ",e)
finally:
    conn.close()
    cursor.close()
    print("Mysql is closed")