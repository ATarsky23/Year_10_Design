import tkinter as tk

users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]


root = tk.Tk()


def login():
	#step 1: access the enrty field for user name, and store that in a varaible






	#step 2: access the enrty field for password, and strore that in a varaible


	#step 3: using loop, check if entered user name exits




	#step 4: if name found, chekck if password mathches
	#step 5: if user and pword are same, change screen


	
	
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




#Main interface setup
titleLabel = tk.Label(root, text = "Grade 4 math quiz")

titleLabel.pack()











#f1 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)

#cur_label = tk.Label(f1, text = "Select shape")

#cur_label.pack()


root.mainloop()