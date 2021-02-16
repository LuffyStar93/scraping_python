from flask import Flask, request, render_template
from db import mydb
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/test', methods=["POST"])
def test():
    return 'ma route /test'

@app.route("/shop")
def page():
    cursor = mydb.cursor()
    sql = "SELECT * FROM jordan"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('page1.html', name="max", age=24, len = len(results), results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)