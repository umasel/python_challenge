import os
import csv

months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


os.chdir(os.path.dirname(__file__))

budget_data_csv_path = os.path.join("budget_data.csv")


with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    
    for row in csv_reader:

        count_months += 1

        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            months.append(row[0])

            profit_loss_changes.append(profit_loss_change)

            previous_month_profit_loss = current_month_profit_loss