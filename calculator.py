"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
#will hold requested users calculation to perform
calculation = raw_input("> ")
#print calculation

#......
token = calculation.split(" ")
print token

#determine what mathematical equation to perform based on users first inputted value
if token[0] == "+":
	print add(int(token[1]), int(token[2]))

elif token[0] == "-":
	print subtract(int(token[1]), int(token[2]))
else:
	print "what?"