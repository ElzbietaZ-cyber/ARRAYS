# Monthly expenses and their corresponding expense categories
# are included in the arrays below.
# Write a program that calculates which expense category was
# the most expensive.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_cost = max(expenses)
max_index = expenses.index(max_cost)
max_category = categories[max_index]

print(max_category)