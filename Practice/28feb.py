#1
'''
def shout(text): 
	return text.upper() 
	
print(shout('Hello')) 
	
yell = shout 
	
print(yell('Hello'))
'''

#2
'''
def shout(text): 
	return text.upper() 

def whisper(text): 
	return text.lower() 

def greet(func): 
	# storing the function in a variable 
	greeting = func("Hi, I am created by a function passed as an argument.") 
	print(greeting) 

greet(shout) 
greet(whisper)
'''


