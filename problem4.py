#!/bin/env python

#Open file
filename = '/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv'
file = open(filename, 'r')

#Use a for loop to look at each waterlevel values
previous = None
n = 0
for line in file:
	reading = line.split(',')
	n = n+1
	#Check if waterlevel is recorded
	for i in range(len(reading)):
		if reading[(i==1)]=='':
			print(n)
			print("Warning! No water level reading was recorded ar this time.")
	
	#Convert the waterlevel readings into numeric values
	try:
		reading1 = float(reading[1])
	except:
		continue

	#Water level limit
        if (reading1>5.0):
		print(n)
                print("Warning! The water level is over 5.0.")

	#Changes in Waterlevel
	if (previous):
		change = reading1-previous
		if (change>=0.25):
			print(n)
			print("Warning! The water level increased more than 0.25 since the previous recording.")
	previous = reading1
