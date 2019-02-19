import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#variables

months = []
profit_loss = []
pybank ={}
average_change = 0
total_months = 0 
net_total = 0

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

#add values to lists
        for row in reader:
            month = row[0]
            months.append(month)
            values = int(row[1])
            profit_loss.append(values)

total_months = len(months)

#find the average change in profits 
net_total = 0

def average(profit_loss):
    length = len(profit_loss)
    net_total = sum(profit_loss)
    return net_total /length 

net_total = sum(profit_loss)
average_change = int(average(profit_loss))

min_profit_loss = profit_loss[profit_loss.index(min(profit_loss))]
max_profit_loss = profit_loss[profit_loss.index(max(profit_loss))]

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} (${max_profit_loss})')
print(f"Greatest Descrease in Profits: {months[profit_loss.index(min(profit_loss))]} (${min_profit_loss})")

output_file = '../PyBank/financial_analysis.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Months: {total_months}"])
    csvwriter.writerow([f"Total: ${net_total}"])
    csvwriter.writerow([f"Average Change: ${average_change}"])
    csvwriter.writerow([f'Greatest Increase in Profits: {months[profit_loss.index(max(profit_loss))]} (${max_profit_loss})'])
    csvwriter.writerow([f"Greatest Descrease in Profits: {months[profit_loss.index(min(profit_loss))]} (${min_profit_loss})"])