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

#user provided input
annual_salary = int(input("Enter your starting annual salary: $"))

#fixed variables
total_cost = 1000000
portion_down_payment = 0.25
down_payment = total_cost * portion_down_payment
current_savings = 0.0
r = 0.04
monthly_r = r / 12
semi_annual_raise_months = 6
semi_annual_raise = 0.07
months_goal = 36

#setup for the bisection
high = 10000
low = 0
epsilon = 100 #acceptable margin of error for the answer
step_count = 0

while True:
    step_count += 1
    portion_saved = (high + low) // 2 #note to self: "//" is floor division.  In other words, only the integer is returned
    working_salary = annual_salary
    working_savings = current_savings
    for months in range(1,months_goal+1):
        working_savings += ((working_salary/12) * (portion_saved / 10000)) + (working_savings*r/12)
        if  months % semi_annual_raise_months == 0:
            working_salary *= 1 + semi_annual_raise #note to self: the "*=" operator multiplies everything on the right by the left and THEN performs the math (addition in this case)
    if abs(working_savings - down_payment) <= epsilon:
        print("The best savings rate to make your downpayment in 36 months is:", (portion_saved/100), "% or", (portion_saved / 10000))
        print("Steps in bisection search:", step_count)
        break
    elif abs(working_savings - down_payment) > epsilon and working_savings > down_payment:
        high = portion_saved
    elif abs(working_savings - down_payment) > epsilon and working_savings < down_payment:
        low = portion_saved
    if low == high:
        print("you can't pay this down in 3 years with you your current salary")
        break