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
    sql="update student set name='Pham Tang' where Code='456'"
    cursor.execute(sql)

    conn.commit()

    print(cursor.rowcount," record(s) affected")

except mysql.connector.Error as e:
    print("Error = ",e)
finally:
    conn.close()
    cursor.close()
    print("Mysql is closed")