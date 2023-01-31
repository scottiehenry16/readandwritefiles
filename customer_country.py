import csv

infile = open('customers.csv', 'r')
reader = csv.reader(infile)
next(reader)

outfile = open('customer_country.csv', 'w', newline = '')
writer = csv.writer(outfile, delimiter = ',')

fieldnames = ['First Name','Last Name','Country']
writer.writerow(fieldnames)

for row in reader:
    first_name = (row[1]) 
    last_name = (row[2])
    country = (row[4])
    
    display = [first_name, last_name, country]
    writer.writerow(display)

infile.close()
outfile.close()