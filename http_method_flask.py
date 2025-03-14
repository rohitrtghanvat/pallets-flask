from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
    return 'welcome %s' % name

@app.route('/login', methods=["get"])
def login():
    user = request.args.get("nm")  # Getting 'nm' from the query string
    return f"Welcome, {user}!"

if __name__ == '__main__':
    app.run(debug=True)