import csv

file = open('epas208it6\Ch8\data.csv', 'r')
csvCursor = csv.DictReader(file)

for row in csvCursor:
    print(row['name'], row['score'])
    
file.close()
