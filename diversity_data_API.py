import requests
import json
from pprint import pprint

fname = input("What is the first name: ")
lname = input("What is the last name:")

#resp = requests.get("https://api.diversitydata.io/?fullname="+fname+"%20"+lname)
resp = requests.get("https://jsonplaceholder.typicode.com/posts")

data = resp.json()
pprint(data)