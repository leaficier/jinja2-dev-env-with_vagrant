#from flask import Flask, redirect, url_for, request, send_from_directory, render_template
from flask import *

app = Flask(__name__, template_folder='templates')

# home page
@app.route('/')
def main():
    return send_from_directory('html','index.html')

@app.route('/user/<username>')
def index(username):
    return render_template('nickshome.html', username=username)

# login form
@app.route('/login')
def login1():
    return send_from_directory('html','login.html')

# login redirection
@app.route('/login', methods=['POST', 'GET'])
def login2():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

# successful login landing page
@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
