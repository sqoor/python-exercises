from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'abc'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/addnew')
def add_new():
    return render_template('student.html')


@app.route('/addRecord', methods=['POST', 'GET'])
def addRecord():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name,address,city,pin)VALUES(?,?,?,?)", (name, address, city, pin))
                con.commit()
                msg = "Record successfully added"""
        except:
            con.rollback()
            msg = "error is insert operation"

        finally:
            return render_template('result.html', msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template('list.html', rows=rows)


if __name__ == '__main__':
    app.run()
