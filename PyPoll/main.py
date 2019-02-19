import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

total_votes = []
count_correy = 0
count_khan = 0 
count_li = 0
count_otooley = 0 
khan_percent = 0
correy_percent = 0 
li_percent = 0
otooley_percent = 0 

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            votes = row[0]
            total_votes.append(votes)
            if row[2] == "Correy":
                count_correy = count_correy + 1 
            elif row[2] == "Khan":
                count_khan = count_khan + 1 
            elif row[2] == "Li":
                count_li = count_li + 1 
            else:
                count_otooley = count_otooley + 1

total_votes = len(total_votes)

khan_percent = (count_khan / total_votes)*100
khan_percent = round(khan_percent, 3)
correy_percent = (count_correy /total_votes)*100
correy_percent = round(correy_percent, 3)
li_percent = (count_li / total_votes) * 100 
li_percent = round(li_percent, 3)
otooley_percent = (count_otooley / total_votes) * 100
otooley_percent = round(otooley_percent, 3)

print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"Khan: {khan_percent}% ({count_khan})")
print(f"Correy: {correy_percent}% ({count_correy})")
print(f"Li: {li_percent}% ({count_li})")
print(f"O'Tooley: {otooley_percent}% ({count_otooley})")
print("--------------------")
print(f"Winner: Khan ")
print("--------------------")

output_file = '../PyPoll/election_results.txt'
with open(output_file, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Khan: {khan_percent}% ({count_khan})"])
    csvwriter.writerow([f"Correy: {correy_percent}% ({count_correy})"])
    csvwriter.writerow([f"Li: {li_percent}% ({count_li})"])
    csvwriter.writerow([f"O'Tooley: {otooley_percent}% ({count_otooley})"])
    csvwriter.writerow(["--------------------"])
    csvwriter.writerow([f"Winner: Khan"])
    csvwriter.writerow(["--------------------"])