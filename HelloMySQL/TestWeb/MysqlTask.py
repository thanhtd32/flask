import json

from flask import Flask, render_template, request,  redirect, url_for
import json
from connector.StudentConnector import StudentConnector
from data.Student import Student

app=Flask(__name__)
@app.route("/")
def main():
    return  render_template("mysql.html")
@app.route("/students/")
def students():
    sconn=StudentConnector()
    students=sconn.get_list_students()
    return render_template("students.html",students=students)
@app.route("/students_json/")
def students_json():
    sconn = StudentConnector()
    students = sconn.get_list_students()
    jsonStr = json.dumps([obj.__dict__ for obj in students])
    return jsonStr
@app.route("/showsignup")
def showsignup():
    return render_template("createstudent.html")
@app.route("/signup",methods=['POST','GET'])
def signup():
    code=request.form["Code"]
    name = request.form["Name"]
    sconn = StudentConnector()
    result=sconn.insert_student(Student(-1,code,name))
    return result
    #return redirect(url_for('students'))
    #return redirect('/students')
@app.route("/students_remove/")
def studentsremove():
    sconn = StudentConnector()
    students = sconn.get_list_students()
    return render_template("students_for_delete.html", students=students)
@app.route("/confirmremovestudent",methods=['POST','GET'])
def confirmremovestudent():
    ID = request.args.get('ID')
    sconn = StudentConnector()
    result=sconn.remove_student(int(ID))
    return  "result"
if __name__ =='__main__':
    app.run(host="localhost",port=9090,debug=True)