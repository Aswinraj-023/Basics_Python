# 3) Calculating the total number of rows needed for parking cars
total_space = 80
each_row_space = 4
total_rows = total_space/each_row_space
print("Total no: of rows for Car Park : ",total_rows)
print("\n---------------------------------------------------------------------------------------")
# Calculation of the remaining pens
total_pens = int(input("Enter the total no: of pens to be sold : ")) # Getting input from user
sold_to_uncle = int(input("Enter the no: of pens sold to uncle : "))
sold_to_cousin = int(input("Enter the no: of pens sold to cousin : "))
sold_to_friend = int(input("Enter the no: of pens sold to friend : "))
remaining_pens = total_pens-(sold_to_uncle+sold_to_cousin+sold_to_friend) # calculating the remaining pens
print("Remaining pens to be sold : ",remaining_pens)
