from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return {"message":"Home Route"}

@app.route('/codechef')
def codechef():
    print("Codechef")


if __name__ == '__main__':
    app.run(debug=True)