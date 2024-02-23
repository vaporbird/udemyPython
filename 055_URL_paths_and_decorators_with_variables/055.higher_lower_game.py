from flask import Flask
import os
from random import randint
app = Flask(__name__)

correct_number = randint(1, 9)
print(correct_number)
colors = ["#F39F18",
          "#6D3F5B",
          "#316650",
          "#6C6960",
          "#D36E70",
          "#1D1E33",
          "#8F8B66",
          "#2D572C",
          "#293133u",
          "#7FB5B5",]


@app.route('/')
def index():
    return "<h1>Guess a number between 0 and 9 by typing it in the URL</h1>" \
           '<div><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt="1 to 9 gif" style="width:300"/></div>'


@app.route('/<bad_input>')
def bad_input(bad_input):
    return f"<span>404 URL for [{bad_input}] not found, Please use only the numbers 1 to 9</span>" \
            '<div><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3k5NHhrN3Bla3V3NjF3MG5lbnR5ZXNkcHp6Y2VwZXdmbzBoaHY1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw' \
            '/fqst7AVqF6AVLlYklE/giphy.gif" alt="1 to 9 gif "style="width:300"/></div>'


@app.route('/<int:number>')
def good_input(number):
    if number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return f"<span>404 URL for [{number}] not found, Please use only the numbers 0 to 9</span>" \
            '<div><img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3k5NHhrN3Bla3V3NjF3MG5lbnR5ZXNkcHp6Y2VwZXdmbzBoaHY1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw' \
            '/fqst7AVqF6AVLlYklE/giphy.gif" alt="1 to 9 gif "style="width:300"/></div>'

    if number > correct_number:
        return f"<span style='color:{colors[number]}'>your guess [{number}] is higher than the target, try again</span>" \
           '<div><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" alt="1 to 9 gif "style="width:300"/></div>'
    elif number < correct_number:
        return f"<span style='color:{colors[number]}'>your guess [{number}] is lower than the target, try again</span>" \
           '<div><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" alt="1 to 9 gif" style="width:300"/></div>'
    elif number == correct_number:
        return f"<span style='color:{colors[number]}'>your guess [{number}] is correct" \
                '<div><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" alt="1 to 9 gif" style="width:300"/></div>'


#  if the file is imported this would not do
if __name__ == "__main__":
    app.run()
