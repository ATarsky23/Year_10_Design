import requests
import json
import tkinter as tk


#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)
#resp = requests.get('https://jsonplaceholder.typicode.com/comments')


#Converts response to JSON
data = resp.json()

#print (data["timestamp"])
#print (data["base"])
#print (data["rates"]["CAD"])

country = []
value = []

#loops through 
for key in data("rates"):
	print(key, ":", data["rates"][key])


root = tk.Tk()#Creates main window for GUI program
# Build in here
#Step 1: Contrust the widget/object
#Step 2: Configure widget/object
#Step 3: Place it on frame/main window

lab = tk.Label(root, text = "Select Country")#Construction


var = tk.StringVar(root)
var.set(country[0])
option_menu = tk.OptionMenu(root, var, "one", "two")
option_menu.pack()



lab.pack()#placing


root.mainloop()#Executes an infinante loop waiting for the user to do something
print("END")