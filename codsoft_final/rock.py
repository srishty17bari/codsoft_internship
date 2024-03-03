from tkinter import *
import random
root = Tk()
root.geometry("600x400")
root.title("Rock Paper Scissor Game")
root.config(bg="black")
computer_value = {
	"0": "Rock",
	"1": "Paper",
	"2": "Scissor"
}
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text="Player			 ")
	l3.config(text="Computer")
	l7.config(text="")
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"
def isrock():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "It's a Tie!!!"
	elif c_v == "Scissor":
		match_result = "Player Win!!!"
	else:
		match_result = "Computer Win!!!"
	l7.config(text=match_result)
	l4.config(text="Rock		 ")
	l6.config(text=c_v)
	button_disable()
def ispaper():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Paper":
		match_result = "It's a Tie!!!"
	elif c_v == "Scissor":
		match_result = "Computer Win!!!"
	else:
		match_result = "Player Win!!!"
	l7.config(text=match_result)
	l4.config(text="Paper		 ")
	l6.config(text=c_v)
	button_disable()
def isscissor():
	c_v = computer_value[str(random.randint(0, 2))]
	if c_v == "Rock":
		match_result = "Computer Win!!!"
	elif c_v == "Scissor":
		match_result = "It's a Tie!!!"
	else:
		match_result = "Player Win!!!"
	l7.config(text=match_result)
	l4.config(text="Scissor		 ")
	l6.config(text=c_v)
	button_disable()
Label(root,
	text="Rock Paper Scissor",
	font="normal 20 bold",
	fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame,
		text="Player			 ",
		font=10)

l2 = Label(frame,
		text="VS			 ",
		font="normal 10 bold")

l3 = Label(frame, text="Computer", font=10)
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

frame2=Frame(root)
frame2.pack()

l4 = Label(frame2,
		text="      			",
		font=10)

l5 = Label(frame2,
		text="VS             ",
		font="normal 10 bold")

l6 = Label(frame2, text="", font=10)



l4.pack(side=LEFT)
l5.pack(side=LEFT)
l6.pack(side=RIGHT)

l7= Label(root,
		text="",
		font="normal 20 bold",
		bg="white",
		width=15,
		borderwidth=2,
		relief="solid")
l7.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock",
			font=10, width=10,bg="white",
			command=isrock)

b2 = Button(frame1, text="Paper ",
			font=10, width=10,bg="white",
			command=ispaper)

b3 = Button(frame1, text="Scissor",
			font=10, width=10,bg="white",
			command=isscissor)

b1.pack(side=LEFT, padx=1)
b2.pack(side=LEFT, padx=1)
b3.pack(padx=1)

Button(root, text="Reset Game",
	font=10, fg="red",
	bg="white", command=reset_game).pack(pady=20)
root.mainloop()
