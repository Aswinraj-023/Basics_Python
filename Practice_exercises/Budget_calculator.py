# 3) Budget calculator
# Getting the expenses details from the user 
salary = float(input("Enter your salary : "))
rent = float(input("Enter the rent amount to be paid : "))
food = float(input("Enter the food expenses : "))
entertainment = float(input("Enter the entertainment expenses : "))
unforeseen = float(input("Enter the unforeseen expenses : "))
# finding the total expenses
total_expenses = rent+food+entertainment+unforeseen
# finding the savings amount
if total_expenses<=salary:
  savings = salary - total_expenses
  print("Total Expenses : ",total_expenses,"\nYour Savings is : ",savings)
else :
  print("Your expenses are greater than your salary","\nSalary : ",salary,"\nTotal Expenses : ",total_expenses)
