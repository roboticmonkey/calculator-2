"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

#will hold requested users calculation to perform
# calculation = None
calculation = raw_input("> ")
while calculation != "q":
	# calculation = raw_input("> ")
	#print calculation

	#......
	token = calculation.split()
	#print token

	#determine what mathematical equation to perform based on users first inputted value
	if token[0] == "+":
		print add(int(token[1]), int(token[2]))

	elif token[0] == "-":
		print subtract(int(token[1]), int(token[2]))

	elif token[0] == "*":
		print multiply(int(token[1]), int(token[2]))
	
	elif token[0] == "/":
		print divide(int(token[1]), int(token[2]))

	elif token[0] == "square":
		print square(int(token[1]))
	
	elif token[0] == "cube":
		print cube(int(token[1]))

	elif token[0] == "pow":
		#test if user inputs a float
		print power(float(token[1]), float(token[2]))

	elif token[0] == "mod":
		print mod(int(token[1]), int(token[2]))	

	else:
		print "what?"

	calculation = raw_input("> ")