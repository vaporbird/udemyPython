from flask import Flask
import os
#os.environ['FLASK_APP'] = 'main.py'
#os.system("flask run")
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<span><strong>H</strong>ello World</span>"

@app.route('/bye')
def bye():
    return "bye"


#  if the file is imported this would not do
if __name__ == "__main__":
    app.run()
