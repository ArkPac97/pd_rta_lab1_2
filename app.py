from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Witaj w moim API!'

@app.route('/mojastrona')
def my_page():
    return 'To jest moja strona!'

if __name__ == '__main__':
    app.run(debug=True)
