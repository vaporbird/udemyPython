from question_model import Question
from data import question_data as questions
from quiz_brain import Brain

question_bank = []
for q in questions:
	question_bank.append(Question(q["text"], q["answer"]))

quiz = Brain(question_bank)

while quiz.still_has_questions():
	quiz.next_question()

print(f"Gz, you completed the quiz\n Your final score is {quiz.score}/{quiz.question_number}")
