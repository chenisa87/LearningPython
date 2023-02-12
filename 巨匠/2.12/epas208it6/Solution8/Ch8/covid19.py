import csv

file = open('covid19_global_cases_and_deaths.csv', 'r', encoding='utf-8')

csvCursor = csv.DictReader(file)
i = 0
print('%15s%12s%10s' %('country','cases','deaths'))
for row in csvCursor:
    print('%15s%12s%10s'
          %(row['country_en'],
            row['cases'],
            row['deaths']))
    i += 1
    if(i>10):
        break

file.close()
