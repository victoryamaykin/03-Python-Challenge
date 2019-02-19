import os
import csv

# Variables
months = []
#profit-loses 
p = []
average_change = 0
total_months = 0 

# Load csv file 
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

# Add values to lists
        for row in reader:
            month = row[0]
            months.append(month)
            values = int(row[1])
            p.append(values)

# Find the total of months in the entire period 
total_months = len(months)

# Find the average of changes in Profits/Losses 
net_total = []

for n in p:
        change = p[n] - p[n - 1]
        net_total.append(change) 

def average(net_total):
    length = len(net_total)
    net_total = sum(net_total)
    return net_total /length 

average_change = int(average(net_total))

# Find the greatest increase/decrease (date and amount) over the entire period
min_p = p[p.index(min(p))]
max_p = p[p.index(max(p))]

# Print out results to console
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})')
print(f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})")

# Create a text file with the results 
output_file = '../PyBank/financial_analysis.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f'Greatest Increase in Profits: {months[p.index(max(p))]} (${max_p})'])
    csvwriter.writerow([f"Greatest Descrease in Profits: {months[p.index(min(p))]} (${min_p})"])