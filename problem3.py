#!/bin/env python

#Read the file 
filename = '/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv'
file = open(filename, 'r')
#Read each line and calculate the maximum rise in water level
max_change = 0
previous = None
for line in file:
	#Split the line into compartments
	reading = line.split(',')
	try:
		reading1 = float(reading[1])

	except:
		continue 

	date_time1 = reading[0]
	if (previous):
		change = reading1-previous
		if (max_change < change):
			max_change = change
			date_time = reading[0]

	previous = reading1 
	
print("", max_change)
print("", date_time) 	
