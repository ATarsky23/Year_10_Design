'''
IsEven takes a single interger paramater a >= 0 returning true if a is even
and false if a is odd.
'''
def IsEven(a):

	if a % 2 == 0:
	 return True

	return False

'''
Test Code
'''
for i in range(0, 100, 1):
	print(IsEven(i))

'''
coding bat solution
'''
def missing_char(str, n):
  
  
 newStr = ""
 newStr = str[0:n] + str[n + 1: len(str)]
 return newStr