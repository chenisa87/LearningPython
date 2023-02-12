import csv

file = open('epas208it6\Ch8\data2.csv', 'r')
fields = ["name","gender","score",
          "age","ageStage","birthday"]

csvCursor = csv.DictReader(file, fields)

for row in csvCursor:
    print(row['name'], row['score'])
    
file.close()
