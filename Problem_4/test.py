import csv
import sys

def main():
	f = open(sys.argv[1],'rt')
	reader = csv.DictReader(f)
	lst = []
	for row in reader:
		lst.append(row)

	print len(lst)
	x = 0
	for index in lst:
		if index['Year'] == None or index['Value'] == None:
			lst.pop(x)
			x = x - 1
		x = x + 1

	print x



if __name__ == '__main__':
	main()