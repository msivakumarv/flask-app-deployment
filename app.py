from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask App!"

@app.route('/status')
def status():
    return "Flask server is running."

if __name__ == '__main__':
    app.run(debug=True)
