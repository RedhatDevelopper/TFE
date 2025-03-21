from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour, ceci est mon site Flask hébergé sur GitHub !"

if __name__ == '__main__':
    app.run(debug=True)