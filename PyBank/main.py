import os
import csv

total_profit = 0
candidates = []
total_votes = []
total_months = 0
total_profit_losses = 0
profit_loss_change = 0
profit_increase = 0

budget_data = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(budget_data) as csv_file:
    csv_reader =csv.reader(csv_file) 
    csv_header = next(csv_reader)

    for row in csv_reader:
        print(row)




