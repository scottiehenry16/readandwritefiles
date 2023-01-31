import csv

infile = open('EmployeePay.csv', 'r')
reader = csv.reader(infile)
next(reader)

for row in reader:
    print('Emplyoee ID:', row[0])
    print('Name:', row[1], row[2]) 
    print('Salary:', '$',format(float(row[3]), ',.2f'))

    salary_value = float(row[3])
    bonus_value = float(row[4])
    calc_bonus = (salary_value * bonus_value)
    print('Bonus:', ' $', format(calc_bonus,',.2f'))

    total_income = (salary_value + calc_bonus)
    print('Total:', ' $', format(total_income, ',.2f'))
    print()

infile.close()