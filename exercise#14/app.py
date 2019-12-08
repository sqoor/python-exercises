from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "This is the Index page"


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/members/<member>')
def members(member):
    return f'Members Page {member}'


@app.route('/scores/<int:scr>')
def scores(scr):
    return render_template('index.html', score=scr)


@app.route('/ex3')
def ex3():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run(debug=False)
