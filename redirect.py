from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html', error=None)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username == 'admin':
            return redirect(url_for('success'))
        else:
            return render_template('login.html', error="Invalid credentials. Try again!")

    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Logged in successfully!'

if __name__ == '__main__':
    app.run(debug=True)
