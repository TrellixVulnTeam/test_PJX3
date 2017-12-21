import csv
reader = csv.reader('c:\\Users\\psoltesz\\bold\\tmp\\eu_accounts.csv', delimiter=',')
print(reader)

for what in reader:
	print(what)
