# In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
# and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
# suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
# How much should you save each month to achieve this?  In this problem, you are going to write a 
# program to answer that question.  To simplify things, assume:
# 3
# 1. Your semi­annual raise is .07 (7%)
# 2. Your investments have an annual return of 0.04 (4%)  
# 3. The down payment is 0.25 (25%) of the cost of the house 
# 4. The cost of the house that you are saving for is $1M.
# You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
# 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
# the required down payment.
annual_salary = int(input("Enter your starting annual salary: $"))
total_cost = int(1000000) #total house cost
portion_down_payment = float(0.25) #percentage down (as a decimal)
down_payment = (total_cost * portion_down_payment) 
r = float(0.04) #return on investments percentage (as decimal)
semi_annual_raise_months = int(6) #number of months for the raise interval
semi_annual_raise = float(0.07) #raise percentage (as decimal)
high = 10000 #initial high limit for the bisection
low = 0 #initial low limit for the bisection
epsilon = 100 #allowable variance "slop" for the search
step_count = int(0)

while True: #this is a deliberate forver loop that we will break with if statements below
    portion_saved = (low + high) / 2 #these three lines are all variables that reset every time the loop runs
    working_salary = annual_salary
    current_savings = 0.0
    for months in range(0,36): #run through a 36 month period to determine how much we will have in savings
        current_savings += ((working_salary/12) * portion_saved) / 10000 + (current_savings*r/12)
        if  months % semi_annual_raise_months == 0:
            working_salary += (working_salary * semi_annual_raise)
    if abs(current_savings - down_payment) <= epsilon: #see if we are less than allowable slop hhave met our target
        print("The best savings rate to make your downpayment in 36 months is:", (portion_saved/100), "% or", (portion_saved / 10000))
        print("Steps in bisection search:", step_count)
        break
    elif abs(current_savings - down_payment) > epsilon and current_savings > down_payment: #we overshot, so adjust the high limit
        high = portion_saved
    elif abs(current_savings - down_payment) > epsilon and current_savings < down_payment: #we undershot, so adjust the low limit
        low = portion_saved
    if low == high:
        print("you can't pay this down in 3 years with you your current salary")
        break
    step_count += 1 #if nothing caugh, itterate and do it again