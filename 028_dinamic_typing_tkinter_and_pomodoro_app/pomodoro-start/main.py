from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
ongoing = False
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_func():
	canvas.itemconfigure(canvas_text, text = "00:00")
	checkmarks.config(text = "✔")
	global timer
	window.after_cancel(timer)
	global reps
	reps = 0

	global ongoing
	ongoing = False

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_func():
	global ongoing
	if not ongoing:
		det_activity()

def det_activity():
	global ongoing
	ongoing = True

	global reps
	reps += 1
	if (reps % 2 == 1):
		activity.config(text = "Working", fg = GREEN)
		countdown(WORK_MIN * 60)
		cm = ""
		for _ in range (1 + int(reps/2)%4):
			cm += "✔"

		checkmarks.config(text = cm)

	elif(reps % 8 != 0):
		activity.config(text = "Break", fg = PINK)
		countdown(SHORT_BREAK_MIN * 60)
	else:
		activity.config(text = "Break", fg = RED)
		countdown(LONG_BREAK_MIN * 60)
	return

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
	if count >= 0:
		canvas.itemconfigure(canvas_text, text = f"{int(count/60):02d}:{int(count%60):02d}")
		global timer
		timer = window.after(1000, countdown, count - 1)
	else:
		det_activity()
	return
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "./tomato.png")
canvas_img = canvas.create_image(101, 112, image = tomato_img)
canvas_text = canvas.create_text(103,130, text = "00:00", fill = "beige", font = ("Times New Roman", 24))
canvas.grid(row = 1, column = 1)

activity = Label(bg = YELLOW, fg = GREEN, font = ("Courier", 32, "bold"), text = "Timer")
activity.grid(row = 0, column = 1)

checkmarks = Label(bg = YELLOW, fg = GREEN, font = ("Courier", 24, "bold"), text = "✔", pady = 20)
checkmarks.grid(row = 3, column = 1)

start = Button(text = "Start", command = start_func, highlightthickness = 0)
start.grid(row = 2, column = 0)

reset = Button(text = "Reset", command = reset_func, highlightthickness = 0)
reset.grid(row = 2, column = 2)

window.mainloop()
