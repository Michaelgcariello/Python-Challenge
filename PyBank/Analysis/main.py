# importing modules
import os

import csv

# making path name to csv file
csvpath = os.path.join('.',"PyBank/Resources/budget_data.csv") 

outputFile = open("budgetData.txt",'x')

# opens csv file
with open(csvpath,'r') as csvfile:

# making file a variable
    budgetdata = (csv.reader(csvfile))

#skip header
    csv_header = next(budgetdata)

    budgetdata_new=list(budgetdata)
    
filename = open(csvpath,'r')
budgetdatalist=csv.DictReader(filename)

#empty lists
month=[]
profit_losses=[]

#for loop to count rows
for col in budgetdatalist:
    month.append(col['Date'])
    profit_losses.append(col['Profit/Losses'])

#printing findings title
print("Financial Analysis")
outputFile.write("Financial Analyis \n")
#printing total months and value
print("Total Months:",len(month))
outputFile.write(f'Total Months: {len(month)} \n')


#finding average total
profitnostring=[eval(i) for i in profit_losses]
print("Total:",sum(profitnostring))
outputFile.write(f'Total: {sum(profitnostring)} \n')


difference_profit_loss=[profitnostring[i+1] - profitnostring[i] for i in range(len(profitnostring)-1)]


#calculating the average change of profit loss
average_change = sum(difference_profit_loss)/len(difference_profit_loss)
print("Average Change:",average_change)
outputFile.write(f'Average Change: {average_change} \n')


#calculating max profit change
max_profit_change=max(difference_profit_loss)

#finding the position/month of the max profit change
position_max_difference=difference_profit_loss.index(max_profit_change)
month_max_difference=month[position_max_difference+1]

#printing max profit month and value
print("Greatest Increase in Profits:",month_max_difference,max_profit_change)
outputFile.write(f'Average Change: {month_max_difference} {max_profit_change} \n')


#calculating min profit change
min_profit_change=min(difference_profit_loss)

#finding the position/month of the min profit change
position_min_difference=difference_profit_loss.index(min_profit_change)
month_min_difference=month[position_min_difference+1]

#printing min profit month and value
print("Greatest Decrease in Profits:",month_min_difference, min_profit_change)
outputFile.write(f'Greatest Decrease in Profits: {month_min_difference} {min_profit_change} \n')


outputFile.close()





