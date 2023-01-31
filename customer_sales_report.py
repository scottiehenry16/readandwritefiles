import csv

infile = open('sales.csv', 'r')
reader = csv.reader(infile)
next(reader)

outfile = open('salesreport.csv', 'w', newline = '')
writer = csv.writer(outfile, delimiter = ',')

fieldnames = ['Customer', 'Total']
writer.writerow(fieldnames)

Total_Sales = 0
CustomerID = 250

for row in reader:
    if int(row[0]) == CustomerID:
        Total_Sales += float(row[3]) + float(row[4]) + float(row[5])
        
    else:
        if CustomerID != 249:
            display = [CustomerID, round(Total_Sales,2)]
            writer.writerow(display)
            
            CustomerID = int(row[0])
            Total_Sales = float(row[3]) + float(row[4]) + float(row[5])

display = [CustomerID, round(Total_Sales,2)]
writer.writerow(display)

infile.close()
outfile.close()