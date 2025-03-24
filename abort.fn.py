from flask import Flask, request, abort, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.abort.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    
    if username != "admin":
        abort(403)  # Forbidden if not admin
    
    return "Welcome, Admin!"

if __name__ == '__main__':
    app.run(debug=True)
