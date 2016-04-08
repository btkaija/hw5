#! /usr/bin/python
#  ECE 2524 Homework 5 Problem 4 Ben Kaija
import sys, math

try:
	name = sys.argv[1]
	f = open(name)
except:
	sys.exit( "unable to open file: "+name)
	
lines = f.readlines()
for l in lines:
	nums = l.split(' ')
	nums = [x for x in nums if x] 
	#print nums
	if 'x1' not in l:
		x = float(nums[2]) - float(nums[0])
		y = float(nums[3]) - float(nums[1])
		#print x, y
		print str(math.sqrt(x**2 + y**2))

print "The number of computed distances is "+str(len(lines)-1)		
