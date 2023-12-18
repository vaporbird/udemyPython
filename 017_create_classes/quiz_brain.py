class Brain:
	def __init__(self, question_bank):
		self.question_number = 0
		self.question_list = question_bank
		self.score = 0

	def next_question(self):
		answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False): ").strip().capitalize()
		self.check_answer(answer, self.question_list[self.question_number].answer)
		self.question_number += 1
		print(f"Your current score is {self.score}/{self.question_number}")
	
	def still_has_questions(self):
		if self.question_number == len(self.question_list):
			return False
		return True
	
	def check_answer(self, user_answer, correct_answer):
		if user_answer == correct_answer: 
			self.score += 1
			print("You guessed correct")
			return True
		print("You guessed wrong")
		return False
		
		
