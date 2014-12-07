import csv

with open('test.csv','r') as csvinput:
	with open('test1.csv','w') as csvoutput:
		reader = csv.reader(csvinput)
		writer = csv.writer(csvoutput)

		all_rows = []
		for row in reader:
			if row[0]=="PassengerId":
				writer.writerow(['PassengerId','Survived'])
			else:
				if row[3]=='female':
					writer.writerow([row[0],'1'])
				else:
					writer.writerow([row[0],'0'])