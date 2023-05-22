import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

#Create variables 
total_months = 0
net_total=0
average_change=0
greatest_increase=0
greatest_decrease=0

#Open and read csv file 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Skip header
    csv_header = next(csvreader)


# Initialize csv.writer
csvwriter = csv.writer(csvfile, delimiter=',')

for row in csvreader:
# Add total months
    total_months.append(row[0])

# Add net total
    net_total.append(row[1])
                     
#Add average change
    average_change.append(row[4])

#Add greatest increase
    greatest_increase.append(row[8])

#Add greatest decrease
    greatest_decrease.append(row[12])

total_months = +-1

# Calculate the overall percent change
length = len(net_total)
total = 0.0

average_change = total/length


 # Print out results
print(f"Budget Results")
print(f"Total months: {str(total_months)}")
print(f"Total: {str(net_total)}")
print(f"Average change: {str(average_change)}")
print(f" Greatest increase {str(greatest_increase)}")
print(f" Greatest decrease {str(greatest_decrease)}")