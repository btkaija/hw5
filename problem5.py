#! /usr/bin/python
#  ECE 2524 Homework 5 Problem 5 Ben Kaija
import sys, math

try:
	name = sys.argv[1]
	f = open(name)
except:
	sys.exit( "unable to open file: "+name)
	
lines = f.readlines()
for l in lines:
	l = l.replace("thee", "you")
	l = l.replace("Thee", "You")
	l = l.replace("thou", "you")	
	l = l.replace("Thou", "You")
	l = l.replace("thy", "your")
	l = l.replace("Thy", "Your")
	l = l.replace("thyself", "youself")
	l = l.replace("Thyself", "Yourself")
	print l[:-1]
	
