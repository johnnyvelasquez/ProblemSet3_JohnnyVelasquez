#!/bin/env python
#Open the file 
filename = '/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv'
file = open(filename, 'r')
#Read each line using for loop and initialize variables
#Minimum water level was set to some arbitrary high value 
min_waterlevel = 1000
max_waterlevel = 0
sum = 0
number_lines = 0
for line in file:
	#Split lines by delimiter to have waterlevel and date separated and start counting sum and line number 
	number_lines = number_lines+1
	reading = line.split(',')
	date_time = reading[0]
	try:
		waterlevel = float(reading[1])
	except:
		continue

	sum = sum+waterlevel
	#Get the max waterlevel
	if (max_waterlevel < waterlevel):
		max_waterlevel = waterlevel
		max_date_time = reading[0]
	#Get the min waterlevel
	if (min_waterlevel > waterlevel):
		min_waterlevel = waterlevel
		min_date_time = reading[0]
#Calculate the average waterlevel
avg_waterlevel = sum/number_lines

#Print statements
print("The minimum water level is", min_waterlevel)
print("It was observed on", min_date_time)

print("The average water level is", avg_waterlevel)

print("The maximum water level is", max_waterlevel)
print("It was observed on", max_date_time)


	
	
 
