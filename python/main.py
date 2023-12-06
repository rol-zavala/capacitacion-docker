from flask import Flask
import os 



app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    variable_env = os.getenv('variable_env') or "NADA"
    return f"Yo soy una App de Python { variable_env }"

if __name__ == '__main__':
    app.run(port=9000)