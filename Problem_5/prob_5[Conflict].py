""" Copyright (C) 2014 by Gurpreet Singh.

 	prob_5.py - Go back to the FAO data from problem 4. Just look at data from 2007. 
 	Make a separate bar graph for each of the continents comparing the number of pigs, 
 	ducks, goats, sheep, cattle, chickents and turkeys. That will be 6 bar graphs with 
 	7 bars each. Now, try to find a way to combine these in a single graph. 
 	How will you show continent vs. animal?
 
	Written by: Gurpreet Singh, 2014. """

import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

# = [chickens, cattles]
Africa = []
Asia = []
AusNZ = []
Europe = []
NA = []
SA = []

def sumzip(*items):
    return [sum(values) for values in zip(*items)]

def readFile(fileName):
	f = open(fileName, 'rt')
	l = []
	try:
	    reader = csv.DictReader(f)	
	    [l.append(row) for row in reader if row["Year"] is not None or row["Value"] is not None]							
	finally:
	    f.close()
	
	return l

def animal_To_Continents(animal):
	for index in animal:
		if (index["Country or Area"] == "Asia +" and index["Year"] == "2007"):
			Asia.append(float(index["Value"]))

		elif (index["Country or Area"] == "Africa +" and index["Year"] == "2007"):
			Africa.append(float(index["Value"]))

		elif (index["Country or Area"] == "Australia and New Zealand +" and index["Year"] == "2007"):
			AusNZ.append(float(index["Value"]))

		elif (index["Country or Area"] == "Europe +" and index["Year"] == "2007"):
			Europe.append(float(index["Value"]))

		elif (index["Country or Area"] == "Northern America +" and index["Year"] == "2007"):
			NA.append(float(index["Value"]))

		elif (index["Country or Area"] == "South America +" and index["Year"] == "2007"):
			SA.append(float(index["Value"]))

def plot(data, title, fig, a):
	fig.add_subplot(2, 3, a)
	N = 7
	width = 0.5
	x = tuple(data)
	ind = np.arange(N)
	plt.yscale('log')
	colors = ['red','yellow','blue','green','magenta','cyan', 'black']
	p1 = plt.bar(ind, x, width, color=colors)
	plt.ylim([10**0,10**10])
	plt.ylabel('Total Population')
	plt.xlabel('Animals')
	plt.xticks(ind, ('chicken', 'cattle', 'duck', 'goat', 'pig', 'sheep', 'turkey'))
	plt.title(title)

def main():
	chicken = readFile("Chickens.csv")
	cattle 	= readFile("Cattles.csv")
	duck 	= readFile("Ducks.csv")
	goat 	= readFile("Goats.csv")
	pig 	= readFile("Pigs.csv")
	sheep 	= readFile("Sheeps.csv")
	turkey 	= readFile("Turkeys.csv")

	# = [chickens, cattles, duck, goat, pig, sheep, turkey]
	animal_To_Continents(chicken)
	animal_To_Continents(cattle)
	animal_To_Continents(duck)
	animal_To_Continents(goat)
	animal_To_Continents(pig)
	animal_To_Continents(sheep)
	animal_To_Continents(turkey)
	
	fig = plt.figure(1, facecolor='w', figsize=(6*3.13,3*3.13))

	left 	= .1
	width 	= 1 - left * 2
	bottom 	= .2
	height 	= 1 - bottom * 1.5
	center 	= 1 - .5	

	plt.figtext(center, height + ((1 - height)/(1.5/1.25)), 
		"Population of Animals in Six Continents in 2007", size='x-large', ha = 'center' )
	
	plt.figtext(center, bottom/20, 
			"Source: FAO Data | Food and Agriculture Organization", 
			ha = 'center')
	
	plot(Africa,'Africa', 		 fig, 1)
	plot(Asia, 	'Asia', 		 fig, 2)
	plot(AusNZ, 'Aus and NZ', 	 fig, 3)
	plot(Europe,'Europe', 		 fig, 4)
	plot(NA, 	'North America', fig, 5)
	plot(SA, 	'South America', fig, 6)
	
	plt.show()

	a = zip(Africa, Asia, AusNZ, Europe, NA, SA)
	
	for i in a:
		print i

	print '_____'
	anm = ['chicken', 'cattle', 'duck', 'goat', 'pig', 'sheep', 'turkey']
	a = sorted(a, key=lambda tup: tup[0]) 		# sort data by continent of the population of animals
	a = sorted(a, key=lambda tup: tup[5])

	for i in a:
		print i
	
	N = 6
	ind = np.arange(N)    	# the x locations for the groups
	width = 0.5       		# the width of the bars: can also be len(x) sequence

	plt.figure(2, facecolor='w', figsize=(6*3.13,3*3.13))
	
	fig.add_axes((left, bottom, width, height))   # [left, bottom, width, height] 

	plt.figtext(center, height + ((1 - height)/(1.5/1.25)), 
			"Population of Animals in Six Continents in 2007", size='x-large', ha = 'center' )
	
	plt.figtext(center, bottom/20, 
				"Source: FAO Data | Food and Agriculture Organization", 
				ha = 'center')

	plt.yscale('log')

	p1 = plt.bar(ind, a[0], width, color='red')
	p2 = plt.bar(ind, a[1], width, color='yellow', 	bottom=sumzip(a[0]) )
	p3 = plt.bar(ind, a[2], width, color='blue', 	bottom=sumzip(a[1], a[0]) )
	p4 = plt.bar(ind, a[3], width, color='green', 	bottom=sumzip(a[2], a[1], a[0]) )
	p5 = plt.bar(ind, a[4], width, color='magenta', bottom=sumzip(a[3], a[2], a[1], a[0]) )
	p6 = plt.bar(ind, a[5], width, color='cyan', 	bottom=sumzip(a[4], a[3], a[2], a[1], a[0]) )
	p7 = plt.bar(ind, a[6], width, color='black', 	bottom=sumzip(a[5], a[4], a[3], a[2], a[1], a[0]) )

	plt.ylabel("Population")
	plt.xlabel("Continents")
	plt.ylim([10**0,10**10])
	plt.xticks(ind+width/2, ('Africa', 'Asia', 'AusNZ', 'Europe', 'NA', 'SA') )
	plt.legend( (p1[0], p2[0], p3[0], p4[0], p5[0], p6[0], p7[0]), ('chicken', 'cattle', 'duck', 'goat', 'pig', 'sheep', 'turkey'))
	plt.legend(loc="upper left", bbox_to_anchor=(1,1))
	plt.show()

	N = 6
	ind = np.arange(N)  	# the x locations for the groups
	width = 0.1       		# the width of the bars

	fig, ax = plt.subplots(facecolor='w', figsize=(6*3.13,3*3.13))
	
	plt.figtext(center, height + ((1 - height)/(1.5/1.25)), 
		"Population of Animals in Six Continents in 2007", size='x-large', ha = 'center' )

	plt.figtext(center, bottom/20, 
			"Source: FAO Data | Food and Agriculture Organization", 
			ha = 'center')

	plt.yscale('log')
	
	rects1 = ax.bar(ind, a[0], width, color='red')
	rects2 = ax.bar(ind+width, a[1], width, color='yellow')
	rects3 = ax.bar(ind+2*width, a[2], width, color='blue')
	rects4 = ax.bar(ind+3*width, a[3], width, color='green')
	rects5 = ax.bar(ind+4*width, a[4], width, color='magenta')
	rects6 = ax.bar(ind+5*width, a[5], width, color='cyan')
	rects7 = ax.bar(ind+6*width, a[6], width, color='black')

	# add some text for labels, title and axes ticks
	ax.set_ylabel('Population')
	ax.set_xlabel('Continents')
	plt.ylim([10**0,10**10])
	ax.set_xticks(ind+width)
	ax.set_xticklabels( ('Africa', 'Asia', 'AusNZ', 'Europe', 'NA', 'SA' ) )
	ax.legend( (rects1[0], rects2[0], rects3[0], rects4[0], rects5[0], rects6[0], rects7[0]), ('chicken', 'cattle', 'duck', 'goat', 'pig', 'sheep', 'turkey'), ncol=7 )
	plt.show()
	

if __name__ == '__main__':
    main()