import os
import csv

# Path to collect data from csv file

budget_data = os. path .join('Resources','budget_data.csv')

# variables set as zero

total_mon = 0

prof_los_amt = 0

diff_val = 0

tot_prof = 0

# Define arrays

months = []
prof_changes = []

with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    header = next(csvreader)


    # first row as base. no change in profit/loss need for this row

    first_row = next(csvreader)

    total_mon = total_mon +1 

    tot_prof = tot_prof + (int(first_row[1]))

    diff_val = int(first_row[1])

   

    #looping through each row

    for row in csvreader:

        total_mon = total_mon + 1

        prof_los_amt = int(row[1])

        tot_prof = tot_prof + prof_los_amt

        prof_diff = prof_los_amt - diff_val


        # add months and pro change to lists

        months.append(row[0])
        prof_changes.append(prof_diff)

        # reset value to calculate the change in profit

        diff_val = int(row[1])

#print(total_mon)
#print(tot_prof)
 # calculate the avreage change over the period

    Average_change= sum(prof_changes) / len(prof_changes)

    #print(Average_change)
          
 # find out the month with max increase      
    greatest_increase = max(prof_changes)
    greatest_index = prof_changes.index(greatest_increase)
    greatest_month = months[greatest_index]


#print(f'{greatest_month} (${str(greatest_increase)})')

# find out the month with maximun deccrese 
    greatest_decrease = min(prof_changes)
    min_index = prof_changes.index(greatest_decrease)
    min_month = months[min_index]

#print(f'{min_month} (${greatest_decrease})')


# format the answers to financial analysis report

print("Financial Analysis")
print ("---------------------------")

print(f'Total Months: {str(total_mon)}')

print(f'Total : ${str(tot_prof)}')

print(f'Average Change : ${str(round(Average_change, 2))}')

print(f'Greatest Increase in Profits : {greatest_month} (${str(greatest_increase)})')

print(f'Greatest Decrease in Profits : {min_month} (${greatest_decrease})')


# Export text files with results

output= open("PyBank_output.txt", "w") 

output.write("Financial Analysis\n")

output.write("-----------------------------\n")

output.write(f'Total Months: {str(total_mon)}\n')

output.write(f'Total : ${str(tot_prof)}\n')

output.write(f'Average Change : ${str(round(Average_change, 2))}\n')

output.write(f'Greatest Increase in Profits : {greatest_month} (${str(greatest_increase)})\n')

output.write(f'Greatest Decrease in Profits : {min_month} (${greatest_decrease})\n')



