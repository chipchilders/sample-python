from flask import Flask
import os

app = Flask(__name__)

cfindex = os.getenv("CF_INSTANCE_INDEX", 0)

svrport = os.getenv('PORT', '5000')

@app.route('/')
def hello_world():
    return 'Hello World! I am instance number ' + str(cfindex)
#os.getenv('VCAP_SERVICES', '')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=svrport)
