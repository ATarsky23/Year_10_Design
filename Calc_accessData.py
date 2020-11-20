import tkinter as tk

root = tk.Tk()


def login():
	print("LOGIN")
	w2.pack_forget()
	w1.pack()

def exit():
	root.destroy()

#Windows
w1 = tk.Frame(root)
w1.config(bg = "orange")

w2 = tk.Frame()
w2.config(bg = "orange")

#LOGIN SETUP


f1w2 = tk.Frame(w2, highlightbackground = "green", highlightthickness=1)
f1w2.config(bg = "green")
f2w2 = tk.Frame(w2, highlightbackground = "green", highlightthickness=1)
f2w2.config(bg = "green")

uName_label = tk.Label(f1w2,text = "User Name: ", bg = "orange")
uName_entry = tk.Entry(f1w2)


pwrd_label = tk.Label(f1w2,text = "Password: ", bg = "orange")
pwrd_entry = tk.Entry(f1w2)

login_btn = tk.Button(f2w2, text = "Login", width = 20, command = login)


uName_label.pack()
uName_entry.pack()
pwrd_label.pack()
pwrd_entry.pack()
login_btn.pack(side = tk.LEFT)


f1w2.pack(fill = tk.X, ipady = 5, ipadx = 5)
f2w2.pack(ipady = 5, ipadx = 5)
w2.pack()















#MAIN INTERFACE SETUP
#frames

f1 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f2 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f3 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)
f4 = tk.Frame(w1)

titleLabel = tk.Label(root, text = "Grade 4 math quiz")
#Frame 1 Setup
# Note everything is being placed in Frame 1 and we are simply packing

cur_label = tk.Label(f1, text = "Select shape")
variable = tk.StringVar(root)
variable.set("one") # default value

cur_select = tk.OptionMenu(f1, variable, "sqaure", "rectangle", "traingle")

cur_label.pack()
cur_select.pack()


#Frame 2 Setup

input1_label = tk.Label(f2, text = "Input Area For Given Shape")
input2_label = tk.Label(f2, text = "L x Width = Height")

item_entry = tk.Entry(f2)
value_entry =tk.Entry(f2)

display = tk.Text(f3, height = 25, width = 60)
display.pack()

total_label = tk.Label(f3, text = "Score Equals = ")
total_label.pack()

input1_label.pack()
input2_label.pack()

item_entry.pack()
value_entry.pack()

info_btn1 = tk.Button(f4, text = "Restart Quiz", width = 25)
info_btn2 = tk.Button(f4, text = "Get Hint", width = 25)
info_btn3 = tk.Button(f4, text = "EXIT", width = 25, command = exit)
info_btn4 = tk.Button(f4, text = "Submit",width = 25)

info_btn1.pack(side = tk.LEFT)
info_btn2.pack(side = tk.LEFT)
info_btn3.pack(side = tk.RIGHT)
info_btn4.pack(side = tk.RIGHT)
#Frame Placements
f1.grid(row = 0, column = 0, sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f2.grid(row = 1, column = 0, sticky = "NESW", padx = 5, pady= 5, ipadx = 2, ipady = 2)
f3.grid(row = 0, column = 1, rowspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
f4.grid(row = 2, column = 0, columnspan = 2,sticky = "NESW", padx = 5, pady = 5, ipadx = 2, ipady = 2)
#w1.pack()

root.mainloop()