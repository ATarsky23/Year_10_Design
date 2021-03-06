import tkinter as tk
import requests
from pprint import pprint
import random


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

root = tk.Tk()

label = tk.Label(root,text = questions[0], bg = "orange")
label.pack()

entry = tk.Entry(root,width = 50, highlightbackground = "orange", highlightthickness=15)
entry.pack()

labelR = tk.Label(root, text = "ENTER AN ANSWER", bg = "orange")
labelR.pack()
labelS = tk.Label(root,text = "Right = " + str(pdata[2]) + " Wrong = " + str(pdata[3]), bg = "orange")

labelS.pack()

btn = tk.Button(root, text = "NEXT", command = next)
btn.pack();



root.mainloop()