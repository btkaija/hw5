#! /usr/bin/python
#  ECE 2524 Homework 5 Problem 6 Ben Kaija
import os
from os.path import isfile, join

path = os.path.dirname(os.path.realpath(__file__))
list = os.listdir(path)
for item in list:
	if isfile(join(path, item)):
		print item+":"
		try:
			f = open(item)
		except:
			sys.exit( "unable to open file: "+name)
	
		lines = f.readlines()
		print lines[0][:-1]
		print lines[1][:-1]

	
