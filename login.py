# create a login page with a username and password input and a login button
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)