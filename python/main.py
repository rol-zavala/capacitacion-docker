from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    return "Yo soy una App de Python"

if __name__ == '__main__':
    app.run(port=9000)