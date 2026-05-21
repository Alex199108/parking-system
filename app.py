from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, from Mac</h1><p>Hot reload merge</p>"

if __name__ == "__main__":
    app.run(debug=True)