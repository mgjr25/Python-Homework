import os
import csv

csvpath = "/Users/MG/Desktop/budget_data.csv"

out_file = "/Users/MG/Desktop/Py Bank.txt"

month_count = 0
month_change_list = []
total_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999]
total_revenue = 0

with open(csvpath, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    header = next(reader)

    first_row = next(reader)
    month_count = month_count + 1
    total_revenue = total_revenue + int(first_row[1])
    revenue_previous = int(first_row[1])

    for row in reader:

# The total number of months included in the dataset

        month_count = month_count + 1

# The total net amount of "Profit/Losses" over the entire period

        total_revenue = total_revenue + int(row[1])

# The average change in "Profit/Losses" between months over the entire period

        revenue_change = int(row[1]) - revenue_previous
        revenue_previous = int(row[1])
        total_change_list = total_change_list + [revenue_change]
        month_change_list = month_change_list + [row[0]]
        



# The greatest increase in profits (date and amount) over the entire period

    
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

# The greatest decrease in losses (date and amount) over the entire period

        if (revenue_change < greatest_increase[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# The average net change

revenue_monthly_avg = sum(total_change_list) / len(total_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"-----------------------------------------------------------------------------\n"
    f"Total Months: {month_count}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${revenue_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits ${greatest_increase[0]} {greatest_increase[1]}\n"
    f"Greatest Decrease in Profits ${greatest_decrease[1]} {greatest_decrease[1]}\n")


print(output)


with open(out_file, "w") as txt_file:
    txt_file.write(output)