import tkinter
w = tkinter.Tk()
w.minsize(600, 400)
w.title("My first GUI")

l = tkinter.Label (text = "Just a basic label", font = ("Arial", 24))
l.pack (side = "bottom")



w.mainloop()
