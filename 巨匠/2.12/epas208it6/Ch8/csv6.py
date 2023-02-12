import csv
header = ['name','address','tel','email','age']
data = [{'name':'Sean', 'address':'123, Oak Street, Taipei', 'tel':'02-9876-5432', 'email':'sean@gmail.com', 'age':40},
        {'name':'Amy', 'address':'456, Park Avenue, Taichung', 'tel':'04-8877-6655', 'email':'amy@gmail.com', 'age':30},
        {'name':'David', 'address':'789 First Road Tainan', 'tel':'06-654-3210', 'email':'david@gmail.com', 'age':25}]

file = open('contact3.csv', 'w')
csvWriter = csv.DictWriter(file, header, dialect='unix')
csvWriter.writeheader()
for d in data:
    csvWriter.writerow(d)
file.close()
print('聯絡人輸出至contact3.csv')
