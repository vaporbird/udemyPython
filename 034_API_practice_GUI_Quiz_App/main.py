from question_model import Question
from quiz_brain import QuizBrain
import requests
import html
from ui import Gui

question_bank = []
http = "https://opentdb.com/api.php"
parameters = {
    "amount" : 10,
    "type" : "boolean",
}



request = requests.get(http, params = parameters)
question_data = request.json()["results"]
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
gui = Gui(quiz)

#while quiz.still_has_questions():
#    quiz.next_question()

#print("You've completed the quiz")
#print(f"Your final score was: {quiz.score}/{quiz.question_number}")


