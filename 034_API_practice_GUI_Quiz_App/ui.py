import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain as qb
from time import sleep
THEME_COLOR = "#375362"

class Gui(tk.Tk):
	def __init__(self, quiz: qb):
		super().__init__()
		self.quiz = quiz
		self.title("Quizzler")
		self.minsize(250,300)
		self.config(bg = THEME_COLOR, padx = 25, pady = 25)
		self._score_label()
		self._canvas()
		self._buttons()
		self.get_next_question()

		self.mainloop()
	
	def _score_label(self):
		self.score_label = tk.Label(self, fg = "white", bg = THEME_COLOR, anchor = tk.CENTER, font = ("Arial", 14), text = "Score : 0 / 0")
		self.score_label.grid(row = 0, column = 1)
		
	def _canvas(self):
		self.canvas = tk.Canvas(self, height = 250, width = 300)
		self.canvas.config(bg = "white")
		self.canvas_text = self.canvas.create_text(290, 100, text = "placeholder", font = ("Arial", 16, "italic"), width = 280, fill = "black", anchor = "e")
		self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 10)

	def _buttons(self):
		self.wrong_button = tk.Button(self, highlightthickness = 0, command = self.guess_false)
		self.correct_button = tk.Button(self, highlightthickness = 0, command = self.guess_true)

		self.correct_img = tk.PhotoImage(file = "./images/true.png")
		self.wrong_img = tk.PhotoImage(file = "./images/false.png")

		self.correct_button.config(image = self.correct_img)
		self.wrong_button.config(image = self.wrong_img)

		self.correct_button.grid(row = 2, column = 1)
		self.wrong_button.grid(row = 2, column = 0)

	def get_next_question(self):
		q_text = self.quiz.next_question()
		self.canvas.itemconfigure(self.canvas_text, text = q_text)

	def update_question(self):
		if self.quiz.still_has_questions():
			self.get_next_question()
		else:
			messagebox.showinfo("Final result", f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
			print("You've completed the quiz")
			print(f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
			exit(0)

	def guess_true(self):
		if self.quiz.check_answer("True"):
			self.canvas.config(bg = "lightgreen")
		else:
			self.canvas.config(bg = "lightcoral")
		self.score_label.config(text = f"Score : {self.quiz.score} / {self.quiz.question_number}")
		self._buttons_logic()
			
	def guess_false(self):
		if self.quiz.check_answer("False"):
			self.canvas.config(bg = "lightcoral")
		else:
			self.canvas.config(bg = "lightgreen")
		self.score_label.config(text = f"Score : {self.quiz.score} / {self.quiz.question_number}")
		self._buttons_logic()
			
	def _buttons_logic(self):
		self.disable_buttons()
		self.after(1000, self.reset_canvas_bg)
		self.after(1000, self.update_question)
		self.after(1000, self.enable_buttons)

	def disable_buttons(self):
		self.correct_button.config(state = "disabled")
		self.wrong_button.config(state = "disabled")

	def enable_buttons(self):		
		self.correct_button.config(state = "normal")
		self.wrong_button.config(state = "normal")
		
	def reset_canvas_bg(self):
		self.canvas.config(bg = "white")
