from flask import Flask
#  os.environ['FLASK_APP'] = 'main.py'
#  os.system("flask run")
app = Flask(__name__)


def make_bold(func):
    def wrapper():
        return f"<strong>{func()}</strong>"
    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}</em>"
    return wrapper


def make_underlined(func):
    def wrapper():
        return f"<u>{func()}</u>"
    return wrapper


@app.route('/')
def hello_world():
    return "<span><strong>H</strong>ello World</span>"


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "bye"


#  Setting a varible with <>
@app.route("/<name>")
def greet(name):
    return f"Hello {name.capitalize()}"


if __name__ == "__main__":
    app.run()
