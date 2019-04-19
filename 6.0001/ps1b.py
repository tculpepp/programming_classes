# In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
# your program to include the following
# 1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
# 2. After the 6th month, increase your salary by that percentage.  Do the same after the 12
# th
# th
# month, the 18  month, and so on. 
# Write a program to calculate how many months it will take you save up enough money for a down
# payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2
# 2. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
portion_down_payment = float(0.25)
current_savings = float(0)
r = float(0.04)
month_counter = int(0)
semi_annual_raise_months = int(6)
annual_salary = int(input("Enter your starting annual salary: $"))
portion_saved = float(input("Enter the portion of your salary you will save as a decimal: "))
total_cost = int(input("Enter the cost of your dream home $"))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

while current_savings < (total_cost * portion_down_payment):
    current_savings += (annual_salary/12) * portion_saved + (current_savings*r/12)
    month_counter += 1
    if month_counter % semi_annual_raise_months == 0:
        annual_salary += (annual_salary * semi_annual_raise)
print ("It will take", month_counter, "months to save up a down payment for your dream house.")
