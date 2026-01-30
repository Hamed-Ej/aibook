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

# save the username and password in a file
def save_credentials(username, password):
    with open('credentials.txt', 'w') as f:
        f.write(f'{username}:{password}')

# read the username and password from the file
def read_credentials():
    with open('credentials.txt', 'r') as f:
        return f.read().split(':')

