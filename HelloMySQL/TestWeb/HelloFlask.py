from flask import  Flask

app=Flask(__name__)

@app.route("/")
def main():
    return "Hello Flask"

if __name__ == "__main__":
    app.run(host="localhost",port=9090,debug=True)