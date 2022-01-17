from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return 'demo for git project flask webpage'

app.run(host='0.0.0.0', port=8000)