from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if not name:
        return redirect(url_for("index"))
    else:
        return render_template('hello.html', name=name)