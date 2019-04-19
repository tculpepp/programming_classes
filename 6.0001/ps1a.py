#In Part A, we are going to determine how long it will take you to save enough
# money to make the down payment given the following assumptions:
# 1. Call the cost of your dream home total_cost.
# 2. Call the portion of the cost needed for a down payment portion_down_payment. For
# simplicity, assume that portion_down_payment = 0.25 (25%).
# 3. Call the amount that you have saved thus far current_savings. You start with a current
# savings of $0. 
# 4. Assume that you invest your current savings wisely, with an annual return of r (in other words,
# at the end of each month, you receive an additional current_savings*r/12 funds to put into
# your savings – the 12 is because r is an annual rate). Assume that your investments earn a 
# return of r = 0.04 (4%).
# 5. Assume your annual salary is annual_salary.
# 6. Assume you are going to dedicate a certain amount of your salary each month to saving for 
# the down payment. Call that portion_saved. This variable should be in decimal form (i.e. 0.1
# for 10%). 
# 7. At the end of each month, your savings will be increased by the return on your investment,
# plus a percentage of your monthly salary (annual salary / 12).
# Write a program to calculate how many months it will take you to save up enough money for a down
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.   
# 1
# Your program should ask the user to enter the following variables:
# 1. The starting annual salary (annual_salary)
# 2. The portion of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)

portion_down_payment = float(0.25)
current_savings = float(0)
r = float(0.04)
month_counter = int(0)
annual_salary = int(input("Enter your starting annual salary: $"))
portion_saved = float(input("Enter the portion of your salary you will save as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: $"))

while current_savings < (total_cost * portion_down_payment):
    current_savings = current_savings + (annual_salary/12) * portion_saved + (current_savings*r/12)
    month_counter = month_counter + 1
print ("It will take", month_counter, "months to save up a down payment for your dream house.")
