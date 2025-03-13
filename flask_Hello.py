# from flask import Flask

# app = Flask(__name__)  # Initialize Flask app

# @app.route("/")  # Define a route (URL)
# def home():
#     return "Hello, Flask!"  # Response when visiting "/"

# if __name__ == "__main__":
#     app.run(debug=True)  # Run the app

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellow_world():
  return 'Hello World'

if __name__ == '__main__':
  app.run(debug=True)