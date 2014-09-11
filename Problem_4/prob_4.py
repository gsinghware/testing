""" Copyright (C) 2014 by Gurpreet Singh.

 	prob_4.py - Use the FAO data under live stock to extract time series 
 	for the population of the goats in the continents Africa, North America, 
 	South America, Asia, Europe and Austrailia + New Zeland. Once you have a 
 	time series for each continent make a single line plot where each 
 	continent has a different color. 
 
	Written by: Gurpreet Singh, 2014. """

import csv
import sys
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import pylab

def main():
	_file = []													# list with each row of the csv file
	
	if (len(sys.argv) > 1):										# check if args are provided
		f = open(sys.argv[1], 'rt')								
	else:	
		f = open('data.csv', 'rt')

	try:
	    reader = csv.DictReader(f)								
	    for row in reader:
	    	if row["Year"] is not None or row["Value"] is not None:
	        	_file.append(row)
	finally:
	    f.close()

	population_Africa = []; years_Africa = []
	population_Asia = []; 	years_Asia = []
	population_Aus_NZ = []; years_Aus_NZ = []
	population_Europe = []; years_Europe = []
	population_NA = []; 	years_NA = []
	population_SA = []; 	years_SA = []

	for index in _file:
		if index["Country or Area"] == "Africa +":
			population_Africa.append(index["Value"])
			years_Africa.append(index["Year"])

		elif index["Country or Area"] == "Asia +":
			population_Asia.append(index["Value"])
			years_Asia.append(index["Year"])

		elif index["Country or Area"] == "Australia and New Zealand +":
			population_Aus_NZ.append(index["Value"])
			years_Aus_NZ.append(index["Year"])

		elif index["Country or Area"] == "Europe +":
			population_Europe.append(index["Value"])
			years_Europe.append(index["Year"])

		elif index["Country or Area"] == "Northern America +":
			population_NA.append(index["Value"])
			years_NA.append(index["Year"])

		elif index["Country or Area"] == "South America +":
			population_SA.append(index["Value"])
			years_SA.append(index["Year"])

		else:
			continue

	fig = plt.figure(facecolor='w')

	left = .1
	width = 1 - left * 2
	bottom = .2
	height = 1 - bottom * 1.5

	fig.add_axes((left, bottom, width, height))   # [left, bottom, width, height] 

	center = 1 - .5	
	
	plt.figtext(center, bottom/3, 
				"Source: FAO Data | Food and Agriculture Organization", 
				ha = 'center')

	plt.figtext(center, height + ((1 - height)/(1.5/1.25)), 
				"Goat Population", size='x-large', ha = 'center' )

	plt.plot(years_Africa, population_Africa, label='Africa')
	plt.plot(years_Asia, population_Asia, label='Asia')	
	plt.plot(years_Aus_NZ, population_Aus_NZ, label='Aus and NZ')
	plt.plot(years_Europe, population_Europe, label='Europe')
	plt.plot(years_NA, population_NA, label='NA')
	plt.plot(years_SA, population_SA, label='SA')
	#plt.ylim([0,10**9])
	#plt.yticks(np.arange(0, 10**9, 10**3))
	plt.yscale('log')
	plt.xlabel("Years")
	plt.ylabel("Value")
	plt.legend(loc='lower right')
	plt.show()
	
if __name__ == '__main__':
    main()