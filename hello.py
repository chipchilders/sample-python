"""Cloud Foundry test"""
from flask import Flask
import os

app = Flask(__name__)

cfindex = os.getenv("INSTANCE_INDEX")

@app.route('/')
def hello_world():
    responsestr = 'Hello World! I am instance number ' + str(cfindex)

#    for key in os.environ.keys():
#        responsestr = responsestr + "\n%30s %s \n" % (key,os.environ[key])

    return responsestr

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
