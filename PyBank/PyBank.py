import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

months = []
revenue =[]
rev_change = []
monthly_change = []


with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader,None)

    for row in csvreader:
        months.append(row[0])
        total_months = len(months)

        revenue.append(int(row[1]))
        total_revenue = sum(revenue)
        
        #Revenue
        revenue_int = map(int, revenue)
        total_revenue = (sum(revenue_int))
        print(total_revenue)

        #average change
        i = 0
        for i in range(len(revenue)-1):
            profit_loss=int(revenue[i+1])-int(revenue[i])
            rev_change.append(profit_loss)
        total = sum(rev_change)
        monthly_change = total/len(rev_change)
        print(monthly_change)

        
        #greatest_increase

        profit_increase = max(rev_change)
        print(profit_increase)
        j = rev_change.index(profit_increase)
        month_increase = month [j+1]

        #greatest_decrease

        profit_decrease = min(rev_change)
        print(profit_decrease)
        k = rev_change.index(profit_decrease)
        month_increase = month [k+1]  

        #print analysis

        print('Financial Analysis')
        print("-----------------------")
        print(f"Total Months: {str(total_months)}")
        print(f"Total: {str(total_revenue)}")
        print(f"Average Change: {str(avg_change)}")
        print(f"greatest_increase: {str(greatest_increase)}")
        print(f"greatest_decrease: {str(greatest_decrease)}")

results = os.path.join("output", "PyBank.txt")

with open(results, "w") as textfile:

    csvwriter = csv.writer(textfile)


    