from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
from db import mydb
import logging
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return  redirect(url_for('shop'))

@app.route("/shop")
def shop():
    return render_template('page1.html')

@app.route("/jordan", methods=['GET'])
def jordan():
    cursor = mydb.cursor()
    sql = "SELECT * FROM jordan"
    cursor.execute(sql)
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/login')
def login():
    username = request.args.get('username')
    if( username == None ):
        return ""
    else:
        return username

if __name__ == "__main__":
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    app.run(host="0.0.0.0", port=3000, debug=True)