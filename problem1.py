#!/bin/env python

#The following code will try to do the following:
#Open a file
filename = '/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv'
file = open(filename, 'r')
#Read each line in the csv file. Also initialize variables.
max_waterlevel = 0
for line in file:
	#Split the line by delimiter and store date/time and waterlevel in variables.
	array = line.split(',')
	date_time = array[0]
	waterlevel = array[1]
	#Extract max waterlevel
	if (max_waterlevel < waterlevel):
		max_waterlevel = waterlevel
		date_time = array[0]
print("The max water level is", max_waterlevel)
print("It was observed on", date_time)

	


