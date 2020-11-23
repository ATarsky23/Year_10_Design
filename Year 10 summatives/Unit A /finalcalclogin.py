import tkinter as tk
import requests
from pprint import pprint
import random

users = ["user1", "user2", "user3"]
passwords = ["pass1", "pass2", "pass3"]


#Main interface setup
resp = requests.get("https://raw.githubusercontent.com/ATarsky23/Year_10_Design/master/Year%2010%20summatives/Unit%20A%20/data.json")
data = resp.json()
#pprint(data)



#What we woudl do is read in all the questions and then use them to 
#populate my tkinter

questions = []
answers = []
#pdata[0] --> current Question
#pdata[1] --> current User
#pdata[2] --> Question rigth
#pdata[3] --> Question wrong
pdata = [0,"user1",0,0]

#Taking the JSON data and putting into hte lists questions and answers
#so you can use it in your program
for i in range(0, len(data),1):
	print(data[i]["question"])
	questions.append(data[i]["question"])
	answers.append(data[i]["answer"])



#Set up your tkineter and when you want to display questions use the 
#the list questions

def next(*args):


	#I only want to change the question if the answer is correct
	#Step 1: Get the data from entry
	ans = entry.get()
	


	#Step 2: Check the ans agains the answer 
	print(ans)
	cq = pdata[0]
	if (ans == answers[cq]):
		print("CORRECT")
		labelR.config(text = "CORRECT")
		x = random.randint(0,len(questions) - 1)
		label.config(text = questions[x])
		pdata[2] = pdata[2] + 1
	else:
		labelR.config(text = "WRONG", bg = "orange")
		pdata[3] = pdata[3] + 1

	labelS.config(text = "Right = " + str(pdata[2]) + " Wrong = " + str(pdata[3]), bg = "orange")



def login():
	#step 1: access the enrty field for user name, and store that in a varaible

	




	#step 2: access the enrty field for password, and strore that in a varaible

	
	#step 3: using loop, check if entered user name exits
	
	for i in range(0,len(users),1):
		if (users[i] == users):
			if (passwords[i] == passwords):
				return True




	#step 4: if name found, chekck if password mathches
	#step 5: if user and pword are same, change screen


	
	
	print("LOGIN")
	w2.pack_forget()
	w1.pack()
	

def exit():
	root.destroy()

root = tk.Tk()


#Windows
w1 = tk.Frame(root)
w1.config(bg = "orange")

w2 = tk.Frame(root)
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





label = tk.Label(root,text = questions[0], bg = "orange")
label.pack()

entry = tk.Entry(root,width = 50, highlightbackground = "green", highlightthickness=15)
entry.pack()

labelR = tk.Label(root, text = "ENTER AN ANSWER", bg = "orange")
labelR.pack()
labelS = tk.Label(root,text = "Right = " + str(pdata[2]) + " Wrong = " + str(pdata[3]), bg = "orange")

labelS.pack()

btn = tk.Button(root, text = "NEXT", command = next)
btn.pack();











#f1 = tk.Frame(w1, highlightbackground = "black", highlightthickness=1)

#cur_label = tk.Label(f1, text = "Select shape")

#cur_label.pack()


root.mainloop()