from flask import Flask
import os

app = Flask(__name__)

cfindex = os.getenv("INSTANCE_INDEX")

@app.route('/')
def hello_world():
    return = 'Hello World! I am instance number ' + str(cfindex)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
