import tkinter as tk

w = tk.Tk()
w.title("Mile to Kilometers converter")
w.config(padx = 50, pady = 20)
w.minsize(width = 200, height = 100)

prompt = tk.Entry(width=10)
prompt.insert(tk.END, string="0")
prompt.grid(row = 0, column = 1)

miles = tk.Label(w ,text = "Miles")
miles.grid(row = 0, column = 2)

equal_to = tk.Label(w ,text = "is equal to") 
equal_to.grid(row = 1, column = 0)

result = tk.Label(w ,text = "0") 
result.grid(row = 1, column = 1)

km = tk.Label(w ,text = "Km")
km.grid(row = 1, column = 2)


def calc():
	
	result.config(text = str(round(float(prompt.get().strip()) * 1.6, 2)))

calculate = tk.Button(text="Calculate", command=calc)
calculate.grid(row = 2, column = 1)

tk.mainloop()
