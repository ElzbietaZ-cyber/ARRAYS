# The data below represents monthly expenses divided into categories and weeks.
# 
# Write a program that calculates and prints:
# total expenses for each category
# total expenses for each week
# total expenses for a month

# Weekly expenses for different categories
# [Food, Transport, Utilities]

monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food = 0
transport = 0
utilities =0
week1 = 0
week2 = 0 
week3 = 0
week4 = 0
month = 0

# Calculates expenses
# Use loop statements

i = 0
while i <= (len(monthly_expenses)-1):
    food += monthly_expenses[i][0]
    i +=1

i=0
while i <= (len(monthly_expenses)-1):
    transport += monthly_expenses[i][1]
    i +=1

i=0
while i <= (len(monthly_expenses)-1):
    utilities += monthly_expenses[i][2]
    i +=1

for item in monthly_expenses[0]:
    week1 += item

for item in monthly_expenses[1]:
    week2 += item

for item in monthly_expenses[2]:
    week3 += item

for item in monthly_expenses[3]:
    week4 += item

for row in monthly_expenses:
    for item in row:
        month += item

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:', utilities)
print('Week 1:',week1)
print('Week 2:',week2)
print('Week 3:',week3)
print('Week 4:',week4)
print('---------------')
print('TOTAL:',month)