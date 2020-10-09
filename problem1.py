#!/bin/env python

#The following code will try to do the following:
#Open a file
filename = '/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv'
file = open(filename, 'r')
for line in file:
	extracted_line = file.readline()
	print(extracted_line)
#Read each line
#Report the highest water level and the date and time that it was observed

